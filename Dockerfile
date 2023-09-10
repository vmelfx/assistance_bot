FROM python:3.10-slim-buster

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH="/app/src/:$PYTHONPATH"

RUN apt-get update \
    # dependencies for building Python packages
    && apt-get install -y build-essential \
    # psycopg2 dependencies \
    && apt-get install -y libpq-dev \
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

COPY ./compose/celery/worker/start.sh /start-celeryworker.sh
RUN sed -i 's/\r$//g' /start-celeryworker.sh
RUN chmod +x /start-celeryworker.sh

COPY ./compose/celery/beat/start.sh /start-celerybeat.sh
RUN sed -i 's/\r$//g' /start-celerybeat.sh
RUN chmod +x /start-celerybeat.sh

COPY ./compose/celery/start.sh /start.sh
RUN sed -i 's/\r$//g' /start.sh
RUN chmod +x /start.sh

WORKDIR /app


