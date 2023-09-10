#!/bin/bash

set -o errexit
set -o nounset


celery -A src.application.celery.tasks worker --loglevel=debug