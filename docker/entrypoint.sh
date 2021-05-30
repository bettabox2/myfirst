#!/bin/sh
sed -i "/ALLOWED_HOSTS/c ALLOWED_HOSTS = ['${ALLOWED_HOST}']" myfirst/settings.py
sed -i "/DEBUG = /c DEBUG = ${DEBUG}" myfirst/settings.py

python3 ./manage.py migrate
python3 ./manage.py runserver 0.0.0.0:8000