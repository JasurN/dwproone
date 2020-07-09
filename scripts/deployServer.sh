#!/bin/bash
cd ./frontend &&
  npm install &&
  npm run build &&
  mkdir -p production &&
  cp -r build/* production/ &&
  cd ~/dwproone &&
  pipenv install &&
  pipenv run python ~/dwproone/manage.py makemigrations &&
  pipenv run python ~/dwproone/manage.py migrate &&
  pipenv run python ~/dwproone/manage.py collectstatic --noinput &&
  sudo systemctl restart gunicorn
