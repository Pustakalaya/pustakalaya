#!/usr/bin/env bash
# Purpose: script to deploy app in a single server.


sudo apt-get install redis-server



# Clone a repo
echo "Cloning repo"
git clone https://github.com/Pustakalaya/custompustakalaya pustakalaya

# Create a virtual environment to work with application
sudo pip install virtualenvwrapper
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv pustakalaya

workon pustakalaya

# Install all the necessary modules
pip install -r pustakalaya/src/requirements/requirements_dev.txt

# Mirage a database
# Configure your IDE as per your requirement to run server automatically from your IDE
cd pustakalaya/src
./manage.py migrate --settings=pustakalaya.settings.development

# Create a user for your app
echo "Configure username and password for app"
./manage.py createsuperuser --settings=pustakalaya.settings.development

# Run your application
./manage.py runserver --settings=pustakalaya.settings.development
