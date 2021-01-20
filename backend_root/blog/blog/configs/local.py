from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "0ys$^!*d^!b97t8be^a%u7l_ny#+h$6q#x@uly@z49!95!l*)$"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("NAME"),
        "USER": os.environ.get("USER"),
        "PASSWORD": os.environ.get("PASSWORD"),
        "HOST": os.environ.get("HOST"),
        "PORT": os.environ.get("PORT"),
    }
}
