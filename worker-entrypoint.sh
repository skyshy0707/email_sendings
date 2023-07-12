#!/bin/sh
cd /code/src
celery -A sendings worker --loglevel=debug --concurrency 1 -E --purge