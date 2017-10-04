#!/bin/sh 
sudo gunicorn -w 1 -b 0.0.0.0:8000 ask.wsgi:application
