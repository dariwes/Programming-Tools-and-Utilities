#!/bin/bash
# pipenv shell
case $1 in
  dev)
    python manage.py runserver --settings=education.settings.dev
    ;;
  prod)
    sudo docker pull dariwes/nginx_project
    sudo docker pull dariwes/django_project_prod
    sudo docker-compose -f docker-compose.prod.yml up -d
    sudo
    python manage.py collectstatic --noinput
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver --settings=education.settings.prod
    ;;
esac