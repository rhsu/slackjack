run:
	python slackjack.py

debug:
	python starterbot.py

test:
	pytest test/

uninstall:
	pip uninstall -y -r requirements.txt 

install:
	pip install -r requirements.txt

.PHONY: run install uninstall debug test test-a
