#!/bin/bash
sudo touch emptyFile
git pull &&
pipenv run python manage.py test &&
cd ../dw_frontend &&
  git pull &&
  yarn install &&
  yarn build &&
  mkdir -p ~/dwproone/frontend/production/ &&
  cp -r build/* ~/dwproone/frontend/production/ &&
  cd ~/dwproone &&
  pipenv install &&
  pipenv run python ~/dwproone/manage.py makemigrations &&
  pipenv run python ~/dwproone/manage.py migrate &&
  pipenv run python ~/dwproone/manage.py collectstatic --noinput &&
  sudo systemctl restart gunicorn
