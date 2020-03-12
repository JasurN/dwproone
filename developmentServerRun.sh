#!/bin/bash
sudo systemctl stop nginx
source ~/.bash_profile
python manage.py runserver