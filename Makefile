deploy:
	lsyncd deploy/lsyncd.conf.lua

install:
	sudo bash deploy/install.sh

.PHONY: deploy install
