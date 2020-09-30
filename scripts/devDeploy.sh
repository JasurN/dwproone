#!/bin/bash
pipenv run python manage.py test &&
cd ../dw_frontend &&
  npm install &&
  npm run build &&
  mkdir -p ~/PycharmProjects/dwproone/frontend/production &&
  cp -r build/* ~/PycharmProjects/dwproone/frontend/production/ &&
  cd ~/PycharmProjects/dwproone &&
  pipenv run python manage.py migrate &&
  pipenv run python manage.py collectstatic --noinput