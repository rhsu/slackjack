run:
	python starterbot.py

clean:
	pip uninstall -y -r requirements.txt 

install:
	pip install -r requirements.txt

PHONY: run clean install
