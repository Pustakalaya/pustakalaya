#!/usr/bin/env bash
 sleep 10

NAME=pustakalaya
# Project source directory
SRCDIR=/src

# Sock file as gunicorn will communicate using unix socket
SOCKFILE=$SRCDIR/gunicorn.sock

# User who runs the app
USER=epustakalaya

# the group to run as
GROUP=epustakalaya

# how many worker processes should Gunicorn spawn
NUM_WORKERS=4

# which settings file should Django use
# If you haven't spit your file it should example.settings only
DJANGO_SETTINGS_MODULE=pustakalaya.settings.production

# WSGI module name
DJANGO_WSGI_MODULE=pustakalaya.wsgi


# Export the settings module
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

# Export the python path from virtualenv dir
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# move to src dir !IMPORTANT otherwise it won't work.
cd $SRCDIR

# python manage.py createsuperuser --settings=$DJANGO_SETTINGS_MODULE
gulp sass

# python manage.py collectstatic --noinput
#
# python manage.py makemigrations
#
#
# python manage.py migrate
# python manage.py index_pustakalaya --settings=$DJANGO_SETTINGS_MODULE

# python manage.py runserver 0.0.0.0:8001 --insecure --settings=$DJANGO_SETTINGS_MODULE
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
   --user=$APP_USER   \
  --bind=0.0.0.0:8001 \
  --log-level=debug \
  --log-file=/var/log/gunicorn-error.log
