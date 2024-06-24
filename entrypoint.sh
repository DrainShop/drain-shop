#!/bin/bash


cmd="$@"
echo "waiting for db"

python3 -m manage collectstatic --noinput
python3 -m manage migrate

export DJANGO_SUPERUSER_USERNAME=root
export DJANGO_SUPERUSER_EMAIL=root@example.com
export DJANGO_SUPERUSER_PASSWORD=1234

python3 -m manage createsuperuser --noinput
gunicorn core.wsgi:application --workers 2 --threads 4 --log-level debug --reload -b 0.0.0.0:8000
exec $cmd