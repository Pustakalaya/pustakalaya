#####################
Quick installation
#####################


Install redis server for caching
---------------------------------

.. code-block:: bash

    $ sudo apt-get install redis-server

Install elastic search engine
--------------------------------
Download and install elastic search engine > 5.5 as per OS.

Install an application
------------------------

Create a working directory

.. code-block:: bash

   $ mkdir ~/workspace
   $ cd workspace


Clone a repository
---------------------
.. code-block:: bash


    $ git clone https://github.com/Pustakalaya/custompustakalaya pustakalaya


Create a virtual environment
------------------------------
To create a virtual environment you can use python virtualenv package, if you haven't
install in your machine, install it

`$ sudo pip install virtualenv`

Create and activate virtualenv
-------------------------------

.. code-block:: bash

    $ virtualenv venv -p /usr/bin/python3
    $ source venv/bin/activate

Install project dependencies.
----------------------------------------

.. code-block:: bash

    $ pip install -r pustakalaya/src/requirements/requirements_dev.txt


Configure project settings
-------------------------------
Inside `src/config` directory, copy `config.example.json` to `config.json` and configure your project settings accordingly.
Sample Configuration of `config.json` file.


.. literalinclude:: ../src/config/config.example.json
   :language: json



Run migrations and create super user
--------------------------------------

.. code-block:: bash

    $ cd pustakalaya/src
    $ ./manage.py migrate --settings=pustakalaya.settings.development

    #Create a user for your app
    $ ./manage.py createsuperuser --settings=pustakalaya.settings.development

    # Start local development server
    $ ./manage.py runserver --settings=pustakalaya.settings.development


Compile frontend assets
-------------------------------
Gulp and webapack has been used to compile front-end dependencies

- `Install yarn <https://yarnpkg.com/lang/en/docs/install/>`_.
- Install all the dependencies packages listed on `package.json` file.
    .. code-block::

        yarn

- Compile the sass assets using gulp

    .. code-block::

        gulp sass
