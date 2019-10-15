@echo off

set "DJANGO_DEBUG=True"

echo "Create new migrations based on the changes to models"
python manage.py makemigrations

echo "Apply database migrations"
python manage.py migrate

REM echo "If not available, set admin account"
REM python initadmin.py

echo "Starting server"
python manage.py runserver 0.0.0.0:8000
