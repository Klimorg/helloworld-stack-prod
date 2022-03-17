#!/bin/sh

echo "Waiting for postgres..."

# db here is the service name of the container running the db
while ! nc -z db 5432; do
    sleep 0.1
done

echo "PostgreSQL started"

exec "$@"
