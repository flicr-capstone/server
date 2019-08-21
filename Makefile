deploy:
	lsyncd deploy/lsyncd.conf.lua

run:
	FLASK_APP=app.py FLASK_DEBUG=1 flask run

install:
	sudo bash deploy/install.sh

createcerts:
	openssl req -x509 -newkey rsa:4096 -keyout /etc/ssl/private/flicr.key -out /etc/ssl/certs/flicr.pem -days 365 -nodes

.PHONY: deploy install run createcerts
