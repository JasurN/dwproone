#!/bin/bash
source ~/dwproone/env_dw/bin/activate
source ~/.bash_profile
NAME="${1?Error: no comamand given}"
python ~/PycharmProjects/dwproone/manage.py $NAME