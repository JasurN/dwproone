#!/bin/bash
cd ./frontend2
yarn install
yarn build
source ~/env_dw/bin/activate
source ~/.bash_profile
python manage makemigrations
python manage migrate
python ~/dwproone/manage.py collectstatic --noinput
sudo systemctl restart gunicorn