FROM python:3.7

LABEL MAINTAINER = "Fernando Posser Pinheiro | feerposser"

ENV PYTHONBUFFERED 1
ENV SECRET_KEY -mo8xvm!c#8gqv^7ap_-rfo_k%^me(@=2%#0!=*y18^pjx2@)o
ENV DEBUG 0
ENV DATABASE_NAME mymbahomedb
ENV DATABASE_USER admin
ENV DATABASE_PASSWORD admin
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
#python manage.py createcachetable

# create migrations files
# python manage.py makemigrations

# makemigrations that affects database
# python manage.py migrate"

# create first super user
# python manage.py createsuperuser