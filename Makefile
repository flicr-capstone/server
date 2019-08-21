deploy:
	lsyncd deploy/lsyncd.conf.lua

run: activate
	FLASK_APP=app.py FLASK_DEBUG=1 flask run

install:
	sudo bash deploy/install.sh

activate:
	. venv/bin/activate

.PHONY: deploy install run
