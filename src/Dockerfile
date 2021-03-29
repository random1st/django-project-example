FROM python:3.9-alpine

ARG VERSION=local


RUN apk add --no-cache  --virtual .build-deps \
    gcc  postgresql-dev libstdc++ swig \
    libffi-dev libc-dev

RUN pip install pipenv==2020.11.15

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN echo "APP_VERSION: $VERSION" >> /version.yml


COPY Pipfile* /tmp/
RUN  cd /tmp && pipenv install  --deploy --system --ignore-pipfile --clear


COPY .  /src/

RUN apk add libpq && apk del .build-deps  && rm -rf /root/.cache
