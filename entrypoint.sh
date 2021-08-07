#!/bin/bash
set -e

if [ "$1" = "local" ]; then
    exec python /code/server/manage.py runserver 0.0.0.0:8000
fi
