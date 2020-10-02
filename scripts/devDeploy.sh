#!/bin/bash
pipenv run python manage.py test &&
  cd ../dw_frontend &&
  yarn install &&
  yarn build &&
  mkdir -p ~/PycharmProjects/dwproone/frontend/production &&
  cp -r build/* ~/PycharmProjects/dwproone/frontend/production/ &&
  rm -r build/
cd ~/PycharmProjects/dwproone &&
  pipenv run python manage.py migrate &&
  pipenv run python manage.py collectstatic --noinput
