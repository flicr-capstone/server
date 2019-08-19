#!/usr/bin/env bash

if [[ "$EUID" -ne 0 ]]
  then echo "Please run with sudo"
  exit
fi

systemctl stop flicr
cp deploy/flicr.service /lib/systemd/system
systemctl daemon-reload
systemctl enable flicr
systemctl start flicr

cp deploy/joe.local /etc/nginx/sites-available
ln -s ../sites-available/joe.local /etc/nginx/sites-enabled/joe.local
systemctl restart nginx
systemctl status nginx
