deploy:
	lsyncd deploy/lsyncd.conf.lua

run:
	. venv/bin/activate && python main.py

install:
	sudo bash deploy/install.sh

createcerts:
	openssl req -x509 -newkey rsa:4096 -keyout /etc/ssl/private/flicr.key -out /etc/ssl/certs/flicr.pem -days 365 -nodes

.PHONY: deploy install run createcerts
