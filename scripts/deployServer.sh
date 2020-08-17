#!/bin/bash
sudo touch emptyFile
git pull &&
cd ../dw_frontend &&
  git pull &&
  yarn install &&
  yarn build &&
  mkdir -p ~/dwproone/frontend/production/ &&
  cp -r build/* ~/dwproone/frontend/production/ &&
  cd ~/dwproone &&
  pipenv install &&
  pipenv run python manage.py migrate &&
  pipenv run python manage.py.py test &&
  pipenv run python manage.py collectstatic --noinput &&
  sudo systemctl restart gunicorn
