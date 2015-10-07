import dj_database_url
import os
import sys

from django.conf import global_settings

PROJECT_NAME = "ot_myproject"
PROJECT_SUB_DIR = "ot_myprojectdir"
ADMINS = (("ot_adminname", "ot_adminemail"))

##################### Paths #####################
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_DIR, 'apps'))
sys.path.insert(0, PROJECT_DIR)

##################### Utilities #####################
def get_from_env(name, *args):
    try:
        return os.environ[name]
    except KeyError:
        if args:
            return args[0]
        else:
            raise KeyError(("%s must be set in the environment to run this "
                            "project.") % name)

##################### Environments #####################
DEBUG = True
TEMPLATE_DEBUG = True

DEVELOPMENT = 1
STAGE = 2
PRODUCTION = 3
SITE_ID = int(os.environ.get("DJANGO_SITE_ID", 1))
SITE_NAME = PROJECT_NAME + (' (dev)', ' (stage)', '')[SITE_ID-1]
SITE_DOMAINS = {
    DEVELOPMENT: 'ot_dev_url',
    STAGE: 'ot_stage_url',
    PRODUCTION: 'ot_production_url'}
SITE_DOMAIN = SITE_DOMAINS[SITE_ID]

DEBUG = SITE_ID == DEVELOPMENT
TEMPLATE_DEBUG = SITE_ID == DEVELOPMENT

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_from_env('SECRET_KEY')

ALLOWED_HOSTS = []
for domain in list(SITE_DOMAINS.values())[1:]:
    domain = domain.split(':')[0]
    ALLOWED_HOSTS.extend((domain, 'www.%s' % domain))

##################### Django #####################
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'main',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)
ROOT_URLCONF = '%s.urls' % PROJECT_SUB_DIR
TEMPLATES_ROOT = os.path.join(PROJECT_DIR, "templates")
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_ROOT],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
SETTINGS_AVAILABLE_IN_TEMPLATES = (
    'SITE_NAME', 'SITE_DOMAIN', 'DEFAULT_PROTOCOL')
WSGI_APPLICATION = '%s.wsgi.application' % PROJECT_SUB_DIR


##################### Internationalization #####################
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


##################### Database #####################
DATABASES = {}

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()

# Enable Connection Pooling (if desired)
DATABASES['default']['ENGINE'] = 'django_postgrespool'

##################### HTTP #####################
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

##################### Files #####################
# Static files (CSS, JavaScript, Images)
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

##################### Compressor #####################
COMPRESS_PRECOMPILERS = (
    ('text/jsx', 'mycompressor.react_compressor.ReactFilter'),
)
