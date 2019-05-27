#!/bin/bash
echo "Waiting for DB to fire up...."
./wait-for-it.sh db:5432
echo "Db started"
sleep 4
ls -l
/usr/local/bin/alembic upgrade heads

echo "Hello world"

set -e

if [ "$1" = 'pserve' ]; then
    echo "Starting server...(It worked if you get output after this)"
    pserve pyramid-docker.ini --reload

else
    exec "$@"
fi