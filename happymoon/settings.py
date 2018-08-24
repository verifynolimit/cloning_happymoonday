"""
Django settings for happymoon project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os, re
from django.conf.global_settings import TEMPLATES


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0s%o239vwga=e5xj_y_%50pl+npal7+_o)&ut5**lkik_@kr*5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'store',
    'mypage',
    'goods',
    'subscription',
    'cart',
    'notice_list',
    'reviews',
    'main',
    'el_pagination',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'happymoon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'happymoon','templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',  ## For EL-pagination
            ],
        },
    },
]

WSGI_APPLICATION = 'happymoon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 각 static 파일에 대한 URL Prefix
STATIC_URL = '/static/' # 항상 /로 끝이 나도록 설정
# STATIC_URL = 'http://static.myservice.com/v1/static/' # 다른 서버에 static파일들을 복사했을 시
# FileSystemFinder 를 위한 static 디렉토리 목록
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# 각 디렉토리 별로 나눠져있는 static파일들을 manage.py collectstatic명령을 통해, 아래 디렉토리 경로로 복사
# 개발 당시에는 의미가 없는 설정. 실서비스 배포 전에 static 파일들을 모아서 배포 서버에 복사 STATIC_ROOT = os.path.join(BASE_DIR, '..', 'staticfiles')


# 각 media 파일에 대한 URL Prefix
MEDIA_URL = '/media/'
# MEDIA_URL = 'http://static.myservice.com/media/' 다른 서버로 media 파일 복사시
# 업로드된 파일을 저장할 디렉토리 경로
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# iamport
DEFAULT_TEST_IMP_KEY = 'imp_apikey'
DEFAULT_TEST_IMP_SECRET = ('ekKoeW8RyKuT0zgaZsUtXXTLQ4AhPFW3ZGseDA6bkA5lamv9O'
                           'qDMnxyeB9wqOsuO9W3Mx9YSJ4dTqJ3f')


# 이메일인증 smtp
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'pirogramming@gmail.com'
EMAIL_HOST_PASSWORD = 'django1!'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
USE_TZ = True
TIME_ZONE = 'Asia/Seoul'

