#!/bin/bash

set -e

cd piririm/

gunicorn \
    --workers 12 \
    piririm.wsgi:application \
    --max-requests 100 \
    -t 600 2>&1 > gunicorn-piririm.log
