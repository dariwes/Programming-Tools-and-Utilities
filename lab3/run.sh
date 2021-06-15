#!/bin/bash
# pipenv shell
case $1 in
  dep)
    cd app/Programming-Tools-and-Utilities/lab3
    sudo sh run.sh prod
    ;;
  prod)
    sudo docker pull dariwes/nginx_project:v1.0
    sudo docker pull dariwes/django_project_prod:v1.0
    sudo docker-compose -f docker-compose.prod.yml up -d
    sudo docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input
    sudo docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations --no-input
    sudo docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --no-input
    ;;
esac