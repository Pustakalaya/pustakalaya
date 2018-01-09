#!/usr/bin/env bash
# Script to install postgresql.
# OS: ubuntu 16.04
# Version: 9.5

sudo apt install postgresql -y

# Start postgresql
sudo systemctl start postgresql postgresql-contrib

# Start postgresql on restart
sudo systemctl enable postgresql

# Create database.
sudo su - postgres # (Super user of postgresql)

# Create database pustakalaya using postgres user.
psql

# create database using psql
# CREATE DATABASE pustakalaya

# Create a role(user) to manage this database.
# CREATE USER your_user WITH PASSWORD your_password

# Manage parameters for user.
# ALTER ROLE your_user SET client_encoding TO 'utf8';
# ALTER ROLE your_user SET timezone TO 'UTC';

# Grant privileges to your created user to DB.
# GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;





