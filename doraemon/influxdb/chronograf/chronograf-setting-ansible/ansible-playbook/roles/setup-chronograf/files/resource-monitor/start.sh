#!/bin/sh

exec /venv/bin/docker-compose up --timeout 60 --force-recreate --no-color
