#!/usr/bin/env bash
# Install pdf and image manipulation apps.
sudo apt-get install libmagickwand-dev
sudo apt-get install libmagickcore5-extra

# Install redis server
sudo apt-get install redis-server

# Run celery
celery -A pustakalaya  worker -l info

