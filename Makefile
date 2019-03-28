run:
	python slackjack.py

debug:
	python starterbot.py

test:
	pytest test/

clean:
	pip uninstall -y -r requirements.txt 

install:
	pip install -r requirements.txt

.PHONY: run clean install debug test
