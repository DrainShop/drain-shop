#!/bin/bash


cmd="$@"
cd DrainShop
pwd
echo "waiting for db"
python3 -m manage collectstatic --noinput
python3 -m manage migrate
python3 -m manage createsuperuser --noinput
gunicorn DrainShop.wsgi:application --workers 2 --threads 4 --log-level debug --reload -b 0.0.0.0:8000
exec $cmd
