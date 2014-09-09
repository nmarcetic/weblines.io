"""
Common settings for weblines.io
"""
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS


# Main system directories
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.dirname(PROJECT_ROOT)
SITE_ID = 1

# Common secret key
SECRET_KEY = '#qh$*8ejlyzfp#^-rc_7is6azubqm8gunq)et7t@()*w*o4!=$'

# Apps & middleware
INSTALLED_APPS = (
    # django internals
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # admin panel
    'grappelli',
    'django.contrib.admin',

    # REST framework
    'rest_framework',

    # migration tool
    'south',

    # image processing library
    'photologue',

    # my applications
    'weblines.apps.cms',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# wsgi & url settings
ROOT_URLCONF = 'weblines.urls'
WSGI_APPLICATION = 'weblines.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

# Date & time
TIME_ZONE = 'UTC'
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'staticfiles')
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder'
)

# Templates
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates')
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

# Uploads
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(SITE_ROOT, 'uploads')
PHOTOLOGUE_DIR = 'data'

# Logging
LOG_DIR = os.path.join(SITE_ROOT, 'logs')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'basic': {
            'format': '[%(asctime)s] %(levelname)s '
            '[%(module)s:%(funcName)s:%(lineno)s] %(message)s',
            'datefmt': '%d.%m.%Y %H:%M',
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'weblines.log'),
            'maxBytes': 5*1024*1024,
            'backupCount': 5,
            'formatter': 'basic',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': True,
        },
        'indie': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
        }
    }
}
