"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from tkinter import ALL

# Init environment variables if on my local device
if 'sferg' in os.path.expanduser('~'):
    try:
        from __docs__ import __secrets__
    except Exception as e:
        print(e)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('LOCAL')

ALLOWED_HOSTS = [
  'www.spencerfd.me',
  'spencerfd.fly.dev'
]
if DEBUG:
  ALLOWED_HOSTS.append('localhost')

# Application definition
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.contenttypes',
  'django.contrib.auth',
  'django.contrib.sessions',
  'django.contrib.messages',
  'whitenoise.runserver_nostatic',
  'django.contrib.staticfiles',

  # My Apps
  'home',

  # Third Party
  'captcha',
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': False,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
      ],
    },
  },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {}

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_FINDERS =  [
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'portfolio/static'),
    ("js", os.path.join(STATIC_ROOT, 'js')),
    ("css", os.path.join(STATIC_ROOT, 'css')),
]

# SMPT CONFIG
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sfergusond@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD', '')
DEFAULT_FROM_EMAIL = 'Spencer Ferguson-Dryden <sfergusond@gmail.com>'

DATE_INPUT_FORMATS = '%d/%m/%Y'
RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_KEY', '')
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_SECRET', '')