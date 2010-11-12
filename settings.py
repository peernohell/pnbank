# -*- coding: utf-8 -*-
from pnbank.apps.accounts.csv import transform_transaction

import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG
DEBUG_TOOLBAR = False

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'pnbank.sqlite3'
        #'USER': '',
        #'PASSWORD': '',
        #'HOST': '',
        #'PORT': '',
    },
}

# Old Database Configuration
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'pnbank'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr-FR'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
APP_ROOT = os.path.abspath(os.path.dirname(__file__)) + '/'
MEDIA_ROOT = os.path.join(APP_ROOT, 'public/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/public/'
CSS_DIR = 'css/'
IMG_DIR = 'img/'
JS_DIR = 'js/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/adm_media/'

LOGIN_REDIRECT_URL = '/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%!&le_74+7l+b0o8r#a3=*3&1av2x9k^47a722@4vgav(!4(p9'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django_mobile.loader.Loader',
    #'django.template.loaders.filesystem.load_template_source',
    #'django.template.loaders.app_directories.load_template_source',
    #'django.template.loaders.eggs.load_template_source',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django_mobile.context_processors.flavour",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

MIDDLEWARE_CLASSES = (
    #'django.middleware.locale.LocaleMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'djangodblog.middleware.DBLogMiddleware',
    #'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
		'django_mobile.middleware.MobileDetectionMiddleware',
		'django_mobile.middleware.SetFlavourMiddleware',
    #'django.contrib.csrf.middleware.CsrfMiddleware',
    #'django.contrib.csrf.middleware.CsrfViewMiddleware',
)
if DEBUG_TOOLBAR:
    MIDDLEWARE_CLASSES += (
        'pnbank.externals.debug_toolbar.middleware.DebugToolbarMiddleware',
    )


ROOT_URLCONF = 'pnbank.urls'

ROOT_PATH = os.path.dirname(__file__)
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = ()

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.humanize',

    'compress',
    'csvimporter',
    'django_extensions',
    'qsstats',
    'south',
		'django_mobile',

    'pnbank.apps.accounts',
    'pnbank.apps.core',
)
if DEBUG_TOOLBAR:
    INSTALLED_APPS += (
        'pnbank.externals.debug_toolbar',
    )


## Compress
COMPRESS = True
COMPRESS_AUTO = True
COMPRESS_VERSION = True
COMPRESS_CSS_FILTERS = None

COMPRESS_CSS = {
    'base': {
        'source_filenames': (
            'css/960_24_col.css',
            'css/sprite.css',
            'css/smoothness/jquery-ui-1.8.custom.css',
            'css/base.css',
        ),
        'output_filename': 'css/base.r?.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

COMPRESS_JS_FILTERS = None
COMPRESS_JS = {
    'base': {
        'source_filenames': (
            'js/jquery-1.4.3.min.js',
            'js/jquery-ui-1.8.5.custom.min.js',
            'js/base.js',
        ),
        'output_filename': 'js/base.r?.js',
    },
}

## CSV Importer
CSVIMPORTER_EXCLUDE = [
    'auth',
    'contenttypes',
    'sessions',
    'sites',
    'admin',
    'csvimporter',
]
CSVIMPORTER_DATA_TRANSFORMS = {
    'accounts.transaction': transform_transaction,
}


## South
SOUTH_TESTS_MIGRATE  = False

from local_settings import *
