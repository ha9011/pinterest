

from .base import *

def read_secret(secret_name):
    file = open("/run/secrets/" + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret

# reading .env file

# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )
#
# # reading .env file
# environ.Env.read_env(
#     env_file= os.path.join(BASE_DIR, '.env')
# )
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#
ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


