#!/usr/bin/env bash

# Install java pre-requisites
sudo add-apt-repository ppa:webupd8team/java
sudo apt update
sudo apt install oracle-java8-installer

# To set Oracle JDK8 as default, need to install the "oracle-java8-set-default" package.
sudo apt oracle-java8-set-default

# Install elastic search
sudo apt-get install apt-transport-https

# Elastic package key importing.
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

# Configure repo having version of 5.X
echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-5.x.list

# Install elastic search
sudo apt-get update && sudo apt-get install elasticsearch

# Enable and start elastic search.
sudo systemctl enable elasticsearch.service
sudo systemctl start elasticsearch.service

# Elastic search configuration options.
# /etc/elasticsearch

# Set max and min heap size to 1G else it won't work as JVM use 1G.
# /etc/elasticsearch/jvm.options
# SET:  -Xms1g
# SET   -Xmx1g

# Data path.
# /var/lib/elasticsearch

# Log files
# /var/log/elasticsearch

# Setting information.
# https://www.elastic.co/guide/en/elasticsearch/reference/5.6/deb.html#deb-repo





