#!/usr/bin/env bash

if [[ "$EUID" -ne 0 ]]
  then echo "Please run with sudo"
  exit
fi
cp deploy/janus.plugin.streaming.jcfg /opt/janus/etc/janus
services="flicr gstreamer1 gstreamer2 janus"
systemctl stop $services
cp deploy/*.service /lib/systemd/system
systemctl daemon-reload
systemctl enable $services
systemctl start $services

cp deploy/joe.local /etc/nginx/sites-available
ln -s ../sites-available/joe.local /etc/nginx/sites-enabled/joe.local
systemctl restart nginx
echo Done
