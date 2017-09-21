# Deploy pustakalaya

# Install necessary dependencies
sudo apt-get install redis-server

# If you want to use Index server, download and configure elastic search server 5.5.6 and
# Configure accordingly in pustakalaya/settings/base.py file

# Create a working directory
mkdir ~/workspace
cd workspace

# Clone a repo
git clone https://github.com/Pustakalaya/custompustakalaya pustakalaya

# Create a virtual environment to work with application
virtualenv venv -p /usr/bin/python3

source venv/bin/activate

# Install all the necessary modules
pip install -r pustakalaya/src/requirements/requirements_dev.txt


# Mirage a database
# Configure your IDE as per your requirement to run server automatically from your IDE
cd pustakalaya/src
./manage.py migrate --settings=pustakalaya.settings.development

# Create a user for your app
./manage.py createsuperuser --settings=pustakalaya.settings.development

# Run your application
./manage.py runserver --settings=pustakalaya.settings.development
