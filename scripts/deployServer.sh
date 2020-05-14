#!/bin/bash
source ~/env_dw/bin/activate
source ~/.bash_profiles
cd ./frontend
npm install
npm run build
python ~/dwproone/manage.py collectstatic --noinput
sudo supervisorctl restart dwproone
