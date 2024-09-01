from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

############################################
# Debug
############################################

DEBUG = True
DEBUG_TOOLBAR = True

############################################
# Secret
############################################

SECRET_KEY = 'django-insecure-y0s46b)+7hl-&+ij08f(yn0gx4e!+@jdmqe^chg)mik%mn(1-_'


############################################
# Database
############################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'table_d_db',
        'USER': 'table_user',
        'PASSWORD': 'table_todo',
        'HOST': '127.0.0.1',
        'PORT': '5632',
    }
}

############################################
# Internal IPs
############################################

INTERNAL_IPS = [
    '127.0.0.1'
]

ALLOWED_HOSTS = [
    '127.0.0.1'
]
