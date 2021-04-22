FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y && apt-get install -y gcc libc-dev python-dev libpq-dev postgresql-client && apt autoremove -y

RUN pip install django djangorestframework psycopg2 Pillow

RUN mkdir -p tikalpoc

WORKDIR /tikalpoc

COPY ./tikalpoc .