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

lint:
	flake8 controllers/ models/ services/ test/ utils/

.PHONY: run install uninstall debug test lint
