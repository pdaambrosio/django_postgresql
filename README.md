# Lab Django with PostgreSQL

This lab runs on the Heroku cloud.
However, it can also be executed locally with some changes described below, using PostgreSQL in a container, creating a volume to persist the data.

It is necessary to have docker and docker-compose installed to run the "postgres_compose.yaml" file.

More information about installing both is at the links below.:

* [Docker](https://docs.docker.com/engine/install/ubuntu/)
* [Docker Compose](https://docs.docker.com/compose/install/)

## Requirements

* Docker, Docker Compose, Python 3.9, Python-pip and Django for local deployment
* Create an account at [heroku.com](https://www.heroku.com/)
* install Heroku CLI

## Heroku CLI

For more information on how to install Heroku see this [link](https://devcenter.heroku.com/articles/heroku-cli#download-and-install), but basically the command below can be used.

```shell
sudo snap install --classic heroku
```

If you need to install the snap, see the official documentation... [snapcraft](https://snapcraft.io/docs/installing-snapd)

After installing the Heroku CLI, execute the commands below to deploy the application.:

```shell
heroku login

heroku create django_postgres --buildpack heroku/python

git push heroku master

heroku run python manage.py migrate

heroku run python manage.py createsuperuser
```

## Local Deployment

To perform the local deployment, go to the 'django_postgres/settings.py' file and edit as below...

Comment these lines:

```python
DATABASES = {
    'default': dj_database_url.config()
}
```

Uncomment these lines (remove lines 66 and 77):

```python
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django',
        'USER':'django-user',
        'PASSWORD':'p@ssW0rD',
        'HOST':'localhost',
        'PORT': '5432',
   }
}
"""
```

Once this is done, execute the commands below.:

Note: Docker, Docker Compose, Python 3.9, Python-pip and Django must be installed.

```shell
pip install -r django_postgresql/requirements.txt

docker-compose -f django_postgresql/postgres_compose.yaml up -d

cd django_postgresql

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Afterwards, you can access the addresses 'localhost:8000' and 'localhost:8000/admin'.

Note: To access the '/admin', it will be necessary to pass the username and password of the 'superuser' created previously.