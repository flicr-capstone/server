deploy:
	lsyncd deploy/lsyncd.conf.lua

run:
	. venv/bin/activate && PYTHONPATH="SGVHAK_Rover:SGVHAK_Rover/SGVHAK_Rover" python main.py

install:
	sudo bash deploy/install.sh

createcerts:
	openssl req -x509 -newkey rsa:4096 -keyout /etc/ssl/private/flicr.key -out /etc/ssl/certs/flicr.pem -days 365 -nodes

test:
	python3 -m unittest discover -sv tests

.PHONY: deploy install run createcerts test
