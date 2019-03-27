import os
import time
import re
from slackclient import SlackClient
import logging
from dotenv import load_dotenv

# load .env variables
load_dotenv()

# sets default logging
logging.basicConfig()

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 0.75  # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

global_var = {
    "hello": 0
}

def parse_bot_commands(slack_events):
    """
    Parses a list of events coming from the Slack RTM API to find bot commands.
    If a bot command is found, this function returns a tuple of
    command and channel.
    If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and "subtype" not in event:
            if event["text"] == "register":
                # from pdb import set_trace; set_trace()
                user_id = event["user"]
                # check if global_var contains the user
                if user_id in global_var:
                    slack_client.api_call(
                        "chat.postMessage",
                        channel=event["channel"],
                        text="You are already registered"
                    )
                # register the user
                else:
                    global_var[user_id] = {
                        "money": 100,
                    }
                    slack_client.api_call(
                        "chat.postMessage",
                        channel=event["channel"],
                        text="OK. I registered you."
                    )
            elif event["text"] == "play":
                # from pdb import set_trace; set_trace()
                user_id = event["user"]
                if user_id not in global_var:
                    slack_client.api_call(
                        "chat.postMessage",
                        channel=event["channel"],
                        text="You are not registered"
                    )
                else:
                    global_var[user_id]["money"] -= 10

                    slack_client.api_call(
                        "chat.postMessage",
                        channel=event["channel"],
                        text="A :spades: J :heart: BlackJack! You Win!"
                    )
                    global_var[user_id]["money"] += 20

                    slack_client.api_call(
                        "chat.postMessage",
                        channel=event["channel"],
                        text="You now have %s dollars" % global_var[user_id]["money"]
                    )
            elif event["text"] == "test me":
                global_var["hello"] = global_var["hello"] + 1
                slack_client.api_call(
                    "chat.postMessage",
                    channel=event["channel"],
                    text="test % s" % global_var["hello"]
                )

            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None


def parse_direct_mention(message_text):
    """
    Finds a direct mention (a mention that is at the beginning) in message text
    and returns the user ID which was mentioned. If there is no direct mention
    returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, 
    # the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)


def handle_command(command, channel):
    """
    Executes bot command if the command is known
    """
    # Default response is help text for the user
    default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)

    # Finds and executes the given command, filling in response
    response = None
    # This is where you start to implement more commands!
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
