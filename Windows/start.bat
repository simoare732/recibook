@echo off
cd /d %~dp0
cd project
pipenv run python manage.py runserver --insecure
