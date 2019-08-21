deploy:
	lsyncd deploy/lsyncd.conf.lua

run:
	FLASK_APP=app.py FLASK_DEBUG=1 flask run

install:
	sudo bash deploy/install.sh

.PHONY: deploy install run
