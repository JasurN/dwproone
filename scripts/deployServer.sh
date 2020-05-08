#!/bin/bash
source ~/env_dw/bin/activate
source ~/.bash_profiles
python ~/dwproone/manage.py collectstatic
sudo supervisorctl restart dwproone
cd ../frontend
npm install
npm run build