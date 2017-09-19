#!/usr/bin/env bash
# Purpose: redis server provision

sudo apt-get install redis-server -y
sudo systemctl start redis
sudo systemctl enable redis