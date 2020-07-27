"""
Django settings for Blog project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h7$8=68p^(dv#vi5*&ffb&tl@5r2v=_c4i1=y3y)tkp^(-1(%9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [

    # Need to be before django.contrib.admin
    'admin_interface',
    'colorfield',

    # Default apps
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My apps
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader',
    'hitcount',
    'taggit',
    'taggit_serializer',
    'crispy_forms',
    'sorl.thumbnail',
    'captcha',
    'articles.apps.ArticlesConfig',
    'courses.apps.CoursesConfig',
    'users.apps.UsersConfig',
    'forum.apps.ForumConfig',
]

AUTH_USER_MODEL = 'users.Account'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

RECAPTCHA_PUBLIC_KEY = '6LfmIuwUAAAAADyG3u6nKWlnaNw2xGUFbVx_sXFQ'
RECAPTCHA_PRIVATE_KEY = '6LfmIuwUAAAAAArBOj5KZj_vRvJ_3muPP_luMp41'


CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Hitcount configuration
HITCOUNT_KEEP_HIT_ACTIVE = { 'days': 1 }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_currentuser.middleware.ThreadLocalUserMiddleware', # for saving current user(author)
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

ROOT_URLCONF = 'Blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'users/templates')],
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

WSGI_APPLICATION = 'Blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

########################################################################################
                            ##  CKEDITOR CONFIGURATION ##
########################################################################################
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/" # from another tutorial
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        'toolbar': 'full',
        'width': '100%',
        'height': '100px',
        'tabSpaces': 4,
        'extraAllowedContent': 'iframe[*]',
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autogrow',
            'codesnippet',
            'embed',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
        ]),
    },

    'basic': {
        'skin': 'n1theme',
        'toolbar': 'Basic',
        'toolbar_Basic':[
            ['Bold', 'Italic', 'Underline'], 
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['CodeSnippet', 'Embed'], 
        ],
        'width': '100%',
        'height': '100px',
        'tabSpaces': 4,
        'extraAllowedContent': 'iframe[*]',
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autogrow',
            'codesnippet',
            'embed',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
        ]),
    }

}


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Athens'


USE_I18N = True
USE_L10N = True
USE_TZ = True

# SMTP configuration
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "pythonas.mail@gmail.com"
EMAIL_HOST_PASSWORD = "#ep7776!smtp"

'''
# SMTP configuration for development
# command to initiate development smtp server : python -m smtpd -n -c DebuggingServer localhost:1025
EMAIL_HOST = 'localhost'
EMAIL_PORT = '1025'
'''


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

#LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'login'
