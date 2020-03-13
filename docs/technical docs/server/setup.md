1. In order to setup server please refer `https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04`
2. for gunicorn setup and supervisor refer to `https://rahmonov.me/posts/deploy-a-django-app-to-digitalocean/` 
3. Important don't create socket or service for gunicorn as described in step 1
4. Set up your supervisor config as described in dwproone.conf which is located in this directory
5. Nginx config file is also located in this directory for future setup