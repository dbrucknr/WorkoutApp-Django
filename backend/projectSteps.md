mkdir backend && cd backend/

pipenv install django, djangorestframework
pipenv shell
django-admin startproject server .
* add rest_framework to settings.py

python manage.py startapp users
* create AbstractUser model
* add app to settings.py
* declare Auth user in settings.py

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

configure the env variables
set up Git 