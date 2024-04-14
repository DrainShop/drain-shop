from pathlib import Path
from split_settings.tools import include
from dotenv import load_dotenv
from os import environ

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(str(BASE_DIR.parent) + '\.env')
print(str(BASE_DIR) + '\.env')
print(environ.get("DEBUG"))

include('components/*.py')


SECRET_KEY = 'django-insecure-#7mqy7eh@)gukw#@zinib!xk^n1682@_qo(9pg0xr^6c@au@d8'

if environ.get("DEBUG") == "False":
    DEBUG = False
else:
    DEBUG = True


SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True

CSRF_COOKIE_SETTINGS = True
USE_X_FORWARDED_HOST = True
CSRF_COOKIE_SECURE = True

ROOT_URLCONF = 'DrainShop.urls'

WSGI_APPLICATION = 'DrainShop.wsgi.application'
