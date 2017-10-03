#!/usr/bin/env bash

sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web1/etc/nginx.conf /etc/nginx/sites-enabled/default
