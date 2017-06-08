Django 1.11+ basic project
================================

This is a simple Django 1.11+ basic project with my preferred setup.

## Features

- Django 1.11
- Support Docker (only development container)
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- PostgreSQL database support with psycopg2.
- Integrated with `django-rest-framework`
- Sign in, Sign up, Account Page


Installing using Docker
-----------------------

> You need to have [docker](http://www.docker.com) (1.10.0+) and
[docker-compose](https://docs.docker.com/compose/install/) (1.6.0+) installed.

You can install the application using the following commands:

```sh
git clone https://github.com/igor-chepurnoi/django-basic.git
cd django-basic
cp .env{.dist,}
cp docker-compose.override.yml{.dist,}
docker-compose up --build
```
> In `.env` file your need to set your UID.
> You can get your UID by the following command in the terminal: `id -u <username>`

It may take some minutes to download the required docker images. When
done, you need to apply migrations as follows:

```sh
docker exec -it django-basic-web-container bash
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata project/apps/*/fixtures/*.json
```

After this steps, you need to create `security.py` file in the `project/settings/local` directory with the following content:

```python
ALLOWED_HOSTS = ['0.0.0.0']
```

After this steps, you can access your app from [http://0.0.0.0:8000/](http://0.0.0.0:8000/).

> For enable debug toolbar you need to create `debug_toolbar.py` file in the `project/settings/local` directory with the following content:

```python
INTERNAL_IPS = ['172.24.0.1', ]
# This is a Gateway address of clewo-web-container, you can check it by the following command - docker inspect django-basic-web-container
```