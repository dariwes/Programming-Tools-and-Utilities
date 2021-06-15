#!/bin/bash
# pipenv shell
case $1 in
  prod)
    sudo docker pull dariwes/nginx_project
    sudo docker pull dariwes/django_project_prod
    sudo docker-compose -f docker-compose.prod.yml up -d
    sudo docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input
    sudo docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations --no-input
    sudo docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --no-input
    ;;
esac