#!/usr/bin/env bash

# Purpose: Gunicorn starter
# Author: manojit.gautam@gmail.com

# Name of an application
NAME="Pustakalaya"

# project directory
PROJECTDIR=/www/pustakalaya.org

# django project virutalenv directory
VENVDIR=/www/pustakalaya.org/venv

# Project source directory
SRCDIR=/www/pustakalaya.org/pustakalaya/src

# Sock file as gunicorn will communicate using unix socket
SOCKFILE=$PROJECTDIR/gunicorn.sock

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

# Activate the virtual environment
source $VENVDIR/bin/activate

# Export the settings module
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

# Export the python path from virtualenv dir
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# move to src dir !IMPORTANT otherwise it won't work.
cd $SRCDIR
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec $VENVDIR/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
