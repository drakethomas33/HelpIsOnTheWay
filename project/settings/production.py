"""Production settings and globals."""

from __future__ import absolute_import

from os import environ

from .base import *


GOOGLE_ANALYTICS_KEY = 'UA-44230933-3'  # test property

########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['www.helpisontheway.co.uk', 'helpisontheway.co.uk', 'help-is-on-the-way.herokuapp.com']
########## END HOST CONFIGURATION

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_variable('SECRET_KEY')
########## END SECRET CONFIGURATION

INSTALLED_APPS += ('storages',)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_QUERYSTRING_AUTH = False  # For now lets not do this
AWS_ACCESS_KEY_ID = get_env_variable('AMAZON_S3_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_env_variable('AMAZON_S3_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = get_env_variable('AMAZON_S3_BUCKET')
AWS_PRELOAD_METADATA = True # necessary to fix manage.py collectstatic command to only upload changed files instead of all files
STATIC_URL = ('https://s3.amazonaws.com/%s/' % get_env_variable('AMAZON_S3_BUCKET')) # TODO: annoyingly collectstatic fails on EU buckets, only US standard works. Solution?!
ADMIN_MEDIA_PREFIX = ('https://s3.amazonaws.com/%s/admin' % get_env_variable('AMAZON_S3_BUCKET'))
