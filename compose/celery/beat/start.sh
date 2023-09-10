#!/bin/bash

set -o errexit
set -o nounset

rm -f './celerybeat.pid'
celery -A src.application.celery.tasks beat --loglevel=debug