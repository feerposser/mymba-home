FROM python:3.7

LABEL MAINTAINER ="Fernando Posser Pinheiro"

ENV PYTHONBUFFERED 1
ENV DEBUG 1

WORKDIR /app

COPY ./mymbahome .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py collectstatic --noinput