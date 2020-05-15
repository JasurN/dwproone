#!/bin/bash
source ~/env_dw/bin/activate
source ~/.bash_profile
NAME="${1?Error: no comamand given}"
python ~/dwproone/manage.py $NAME