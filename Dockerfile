FROM python:3.10-slim-buster as base
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc libpq-dev default-libmysqlclient-dev pkg-config \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

# development
FROM base as development
VOLUME /app

# production
FROM base as production
