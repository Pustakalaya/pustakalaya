#!/usr/bin/env bash

# OS: ubuntu 16.04
# Purpose: install and configure nginx
# Description: This script install nginx along with nginx PSM module.

sudo apt-get update -y

# Install build tools.
sudo apt install build-essential -y


# This install nginx automatically and also install dependencies and build the latest mainline version of nginx
# with the latest stable version of ngx_pagespeed, run:

bash <(curl -f -L -sS https://ngxpagespeed.com/install) \
     --nginx-version latest # For more info see: https://www.modpagespeed.com/doc/build_ngx_pagespeed_from_source

# Configuration path
# nginx path prefix: "/usr/local/nginx"
# nginx binary file: "/usr/local/nginx/sbin/nginx"
# nginx modules path: "/usr/local/nginx/modules"
# nginx configuration prefix: "/usr/local/nginx/conf"
# nginx configuration file: "/usr/local/nginx/conf/nginx.conf"
# nginx pid file: "/usr/local/nginx/logs/nginx.pid"
# nginx error log file: "/usr/local/nginx/logs/error.log"
# nginx http access log file: "/usr/local/nginx/logs/access.log"
# nginx http client request body temporary files: "client_body_temp"
# nginx http proxy temporary files: "proxy_temp"
# nginx http fastcgi temporary files: "fastcgi_temp"
# nginx http uwsgi temporary files: "uwsgi_temp"
# nginx http scgi temporary files: "scgi_temp"


# Add nginx executable to bin dir
sudo ln -s /usr/local/nginx/sbin/nginx /usr/sbin/nginx

# Create systemd.
sudo vim /etc/systemd/system/nginx.service

# Start and enable nginx
sudo systemctl start nginx.service && sudo systemctl enable nginx.service

# Copy the configuration file from 'conf/nginx.conf' to /user/local/nginx/conf as nginx.conf

# Create configuration file
# /etc/nginx/sites-available
touch /etc/nginx/pustakalaya

# Change configuration file accordingly. /usr/local/nginx/conf/nginx.conf

# Enable the web app.
sudo ln -s /etc/nginx/sites-available/pustakalaya /etc/nginx/sites-enabled




