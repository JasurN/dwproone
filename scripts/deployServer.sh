#!/bin/bash
cd ./frontend2
npm install
npm run build
mkdir -p production
cp -r build/* production/
cd ~/dwproone
pipenv shell
pipenv install
python ~/dwproone/manage.py makemigrations
python ~/dwproone/manage.py migrate
python ~/dwproone/manage.py collectstatic --noinput
sudo systemctl restart gunicorn