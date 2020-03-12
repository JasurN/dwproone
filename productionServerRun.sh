#!/bin/bash
source ~/dwproone_backend/env_dwproone/bin/activate
source ~/.bash_profile

python ~/dwproone_backend/dwproone/manage.py runserver 0.0.0.0:8000