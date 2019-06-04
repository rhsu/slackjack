# Virtualenv
In the project root directory after cloning run:  `python3 -m virtualenv .` 

Note that you might not have `virtualenv` installed. 
It's recommeded to use `virtualenv` with `python3`

To install `virtualenv`:
run `pip3 install virtualenv`

# .env
after being added as a collaborator, you'll need a `.env` file which can be created via `touch .env`
Put this file in the root directory. The token can be retrieved from this site: https://api.slack.com/apps/AH9DW4PJ8/install-on-team?success=1
In the `.env` file type:

```
SLACK_BOT_TOKEN=<<<Bot User OAuth Access Token Here>>>
```

green-dot icon is not an emoji. To get that feature working, you'll need to configure an environment variable which looks like such:

```
GREEN_ICON=':green-circle:'
```

# Makefile
After setting up the `virtualenv`, all commands can be done through the `Makefile`

To install the app, (you'll need to do this the first time before you run the app), do
`make install`

To run the app, you'll need to start the virtualenv. This can be done by `source bin/activate`. After that run `make run`

To remove the dependencies installed in the `virtualenv`, do `make uninstall`. This command
is rarely used but will be useful once packages are updated in `requirements.txt`
