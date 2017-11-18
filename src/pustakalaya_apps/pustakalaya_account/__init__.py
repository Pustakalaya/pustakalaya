"""
This apps aims to override the django-all-auth package to fit the needs of
pustakalaya authentication.

All the templates of django all auth are overriden here by placing

"""
default_app_config = "pustakalaya_apps.pustakalaya_account.apps.PustakalayaAccountConfig"
