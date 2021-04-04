
from .base import *

def read_secret(secret_name):
    file = open("/run/secrets/"+secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret

# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# 배포에서는 False로
DEBUG = False

#
ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',  # db의 이름
        'USER': 'django', #
        'PASSWORD': read_secret("MYSQL_PASSWORD"),
        'HOST': 'mariadb',   # 컨테이너 이름
        'PORT': '3306',
    }
}
