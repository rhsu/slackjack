run:
	python slackjack.py

debug:
	python starterbot.py

test:
	pytest test/

simulate:
	pytest -s test/services_tests/test_simulation_service.py

uninstall:
	pip uninstall -y -r requirements.txt 

install:
	pip install -r requirements.txt

lint:
	flake8 controllers/ models/ services/ test/ utils/

.PHONY: run install uninstall debug test simulate lint
