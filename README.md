# HackEPS2017

## Setup Development

- Crear virtual environment:

`virtualenv venv`

- Utilizar el virtual env:

`source venv/bin/activate`

- Instalar dependencias:

`pip install -r requirements.txt`

## Instalar / ejecutar DBs

`docker-compose up -d`

`python manage.py migrate`

## Dependencias de sistema

ChromeWebdriver: https://sites.google.com/a/chromium.org/chromedriver/downloads

En OSX: `brew search chromedriver`
