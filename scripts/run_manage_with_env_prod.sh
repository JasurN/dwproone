#!/bin/bash
source ~/env_dw/bin/activate
source ~/.bash_profiles
NAME="${1?Error: no comamand given}"
python ~/dwproone/manage.py $NAME