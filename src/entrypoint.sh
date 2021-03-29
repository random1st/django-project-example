#!/bin/sh

set -exua

if [ ! -z "${WAIT_FOR+x}" ]; then

# wait until a port is binded by some server
# (db, dynamodb etc), because docker-compose's
# depends_on does not guarantee that servers inside
# bind on ports

for i in $(echo $WAIT_FOR | sed "s/,/ /g")
do
    # call your procedure/other scripts here below
    ./wait_for.sh $i -t 15 -- echo "Started $i"
done

fi

if [ ! -z "${MIGRATE+x}" ]; then
python manage.py makemigrations
python manage.py migrate
fi

"$@"