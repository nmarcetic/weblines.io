"""
Development settings for weblines.io
"""
from weblines.settings.common import *

# Activate debug mode
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# South testing
SKIP_SOUTH_TESTS = True

# Development database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'weblines.db'),
    }
}

# framework setup
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),

    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    )
}
