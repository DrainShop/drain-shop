from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_URLCONF = 'core.urls'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
