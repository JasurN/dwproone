source ~/.bash_profile
fuser -k 8000/tcp
python manage.py runserver