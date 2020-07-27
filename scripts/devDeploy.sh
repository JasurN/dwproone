#!/bin/bash
cd ../dw_frontend &&
  yarn install &&
  yarn build &&
  mkdir -p ~/PycharmProjects/dwproone/frontend/production &&
  cp -r build/* ~/PycharmProjects/dwproone/frontend/production/ &&
  cd ~/PycharmProjects/dwproone &&
  pipenv run python manage.py makemigrations &&
  pipenv run python manage.py migrate &&
  pipenv run python manage.py collectstatic --noinput