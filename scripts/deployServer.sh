#!/bin/bash
  sudo touch emptyFile
  git pull &&
  cd ../dw_frontend &&
    git pull &&
    mkdir -p ~/dwproone/frontend/production/ &&
    cp -r build/* ~/dwproone/frontend/production/ &&
    cd ~/dwproone &&
    pipenv install &&
    pipenv run python ~/dwproone/manage.py migrate &&
    pipenv run python ~/dwproone/manage.py test &&
    pipenv run python ~/dwproone/manage.py collectstatic --noinput &&
    sudo systemctl restart erp
