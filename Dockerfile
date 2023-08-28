FROM python:3.10-slim-buster

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
    # dependencies for building Python packages
    && apt-get install -y build-essential \
    # Translations dependencies \
    && apt-get install -y gettext \
    # Additional dependencies
    && apt-get install -y procps telnet \
    # cleaning up unused files \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Requirements are installed here to ensure they will be cached \
RUN pip install --upgrade pip pipenv setuptools
COPY ./Pipfile Pipfile.lock ./
RUN pipenv sync --system ${PIPENV_EXTRA_ARGS}


WORKDIR /app
