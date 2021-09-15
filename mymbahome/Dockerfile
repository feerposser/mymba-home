FROM python:3.7

LABEL MAINTAINER = "Fernando Posser Pinheiro | feerposser"

ENV PYTHONBUFFERED 1
ENV DATABASE_HOST mysql
ENV DATABASE_PORT 3306

WORKDIR /app

COPY ./mymbahome /app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# copy static files to STATIC_ROOT
RUN python manage.py collectstatic --noinput


# after up, need to execute:
# docker exec -it <container_id> /bin/bash
# and run commands bellow

# create key value cache table
# python manage.py createcachetable

# create migrations files
# python manage.py makemigrations

# makemigrations that affects database
# python manage.py migrate

# create first super user
# python manage.py createsuperuser