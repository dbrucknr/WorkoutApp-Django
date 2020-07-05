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

...

docker-compose exec workouts-db psql --username=workout --dbname=workouts_dev
Added the .sh file, change permissions: 'chmod +x ./entrypoint.sh'
Update the Dockerfile to run the shell script, as the container depends on the postgres DB

docker-compose exec workouts pytest