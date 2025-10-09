# project/settings.py
from __future__ import annotations

from os.path import join
from pathlib import Path
from typing import Any

from django.core.handlers.asgi import ASGIRequest
from django.core.handlers.wsgi import WSGIRequest

from .jazzmin import JAZZMIN_SETTINGS as _JAZZMIN_SETTINGS
from .jazzmin import JAZZMIN_UI_TWEAKS

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'hui'
DEBUG = True
ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'app.User'

INSTALLED_APPS = [
    'xldashboard',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'
]

# xl-dashboard
XL_DASHBOARD = {
    'Dashboard': {
        '__name__': '',
        '__background__': '#ff55ee33',
        'Dashboard': {
            'name': 'Dashboard',
            'model': '/admin',
            'background': '#ff55ee',
        }
    },
    'General': {
        'Users SS': {
            'name': 'Users',
            'model': 'app.User',
            'background': '#ffee55',
        },
        'Groups AA': 'auth.Group',
    },
    # 'xl-actions': { # TODO: not working now
    #     'Collect Static': 'run_collectstatic',
    # }
}

# Jazzmin
JAZZMIN_SETTINGS = _JAZZMIN_SETTINGS | {
    'usermenu_links': [
        {'name': 'Site', 'url': f'https://...', 'new_window': True},
        {'name': 'Logs', 'url': f'https://...', 'new_window': True},
    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
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

WSGI_APPLICATION = None
ASGI_APPLICATION = 'project.asgi.application'
DATABASES = {'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
