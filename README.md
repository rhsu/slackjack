# NEWS!
slackjack is now on `python3`. This readme will be updated soon.


# Virtualenv
In the project root directory after cloning run:  `python -m virtualenv .` 

Note that you might not have `virtualenv` installed. 
It's recommeded to use `virtualenv` with Python2.7. Python3 is not supported yet. 

To install `virtualenv`:
run `pip install virtualenv` but make sure that `pip` is pointed to `Python2.7`. You can verify
that with `which pip` which should return

```
$ which pip
/usr/local/bin/pip
```

Important: not `pip3`!

# .env
after being added as a collaborator, you'll need a `.env` file which can be created via `touch .env`
Put this file in the root directory. The token can be retrieved from this site: https://api.slack.com/apps/AH9DW4PJ8/install-on-team?success=1
In the `.env` file type:

```
SLACK_BOT_TOKEN=<<<Bot User OAuth Access Token Here>>>
```

# Makefile
After setting up the `virtualenv`, all commands can be done through the `Makefile`

To install the app, (you'll need to do this the first time before you run the app), do
`make install`

To run the app, you'll need to start the virtualenv. This can be done by `source bin/activate`. After that run `make run`

To remove the dependencies installed in the `virtualenv`, do `make uninstall`. This command
is rarely used but will be useful once packages are updated in `requirements.txt`
