#!/bin/bash
cd ./frontend2
npm install
npm run build
source ~/env_dw/bin/activate
source ~/.bash_profile
python ~/dwproone/manage.py makemigrations
python ~/dwproone/manage.py migrate
python ~/dwproone/manage.py collectstatic --noinput
sudo systemctl restart gunicorn