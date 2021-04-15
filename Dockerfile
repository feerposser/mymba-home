FROM python:3.7

ENV PYTHONBUFFERED 1
ENV DEBUG 1

WORKDIR /mymbahome

COPY ./mymbahome .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py collectstatic --noinput