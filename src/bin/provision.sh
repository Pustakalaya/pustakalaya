#!/usr/bin/env bash

# Install nginx
source ./provision_scripts/nginx.sh

# Install postgresql
source ./provision_scripts/postgresql.sh


# Install Redis
source ./provision_scripts/redis.sh


# Install elastic search
source ./provision_scripts/elasticsearch.sh


# Install supervisor
source ./provision_scripts/supervisor.sh

# Install utilities packages
source ./provision_scripts/utils.sh





