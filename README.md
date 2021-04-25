# Lab Django with PostgreSQL

This lab runs on the Heroku cloud.
However, it can also be executed locally with some changes described below, using PostgreSQL in a container, creating a volume to persist the data.

It is necessary to have docker and docker-compose installed to run the "postgres_compose.yaml" file.

More information about installing both is at the links below.:

* [Docker](https://docs.docker.com/engine/install/ubuntu/)
* [Docker Compose](https://docs.docker.com/compose/install/)

## Requirements

* Docker, Docker Compose and Django for local deployment
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