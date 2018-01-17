#!/usr/bin/env bash
# OS: ubuntu 16.04
# Purpose: install and configure nginx
# Nginx Version 1.10

# Install nginx
sudo apt-get install nginx -y

# Start nginx on restart
sudo systemctl enable nginx

# Create configuration file
# /etc/nginx/sites-available
touch /etc/nginx/pustakalaya

# Enable the web app.
sudo ln -s /etc/nginx/sites-available/pustakalaya /etc/nginx/sites-enabled



