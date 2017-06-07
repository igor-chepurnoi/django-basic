Backend Application
================================

Installing using Docker
-----------------------

> You need to have [docker](http://www.docker.com) (1.10.0+) and
[docker-compose](https://docs.docker.com/compose/install/) (1.6.0+) installed.

You can install the application using the following commands:

```sh
git clone https://bitbucket.org/chepurnoi-igor/clewo-backend-app.git
cd clewo-backend-app
cp .env{.dist,}
cp docker-compose.override.yml{.dist,}
docker-compose up -d --build
```
> In `.env` file your need to set your UID.
> You can get your UID by the following command in the terminal: `id -u <username>`

It may take some minutes to download the required docker images. When
done, you need to apply migrations as follows:

```sh
docker exec -it clewo-web-container bash
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata project/apps/*/fixtures/*.json
```