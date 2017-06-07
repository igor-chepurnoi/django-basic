FROM postgres:9.6

MAINTAINER Igor Chepurnoi <chepurnoi.igor@gmail.com>

ARG HOST_UID=1000

VOLUME ["/var/lib/postgresql/data"]

RUN usermod -u ${HOST_UID} postgres && groupmod -g ${HOST_UID} postgres

EXPOSE 5432