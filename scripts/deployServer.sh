#!/bin/bash
cd ./frontend2
npm install
npm run build
mkdir -p production
cp -r build/* production/
source ~/env_dw/bin/activate
source ~/.bash_profile
cd ~/dwproone
pip install -r requirements.txt
python ~/dwproone/manage.py makemigrations
python ~/dwproone/manage.py migrate
python ~/dwproone/manage.py collectstatic --noinput
sudo systemctl restart gunicorn