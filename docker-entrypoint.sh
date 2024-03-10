#!/bin/bash
python manage.py collectstatic --noinput

python3 manage.py migrate

gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 3