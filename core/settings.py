from pathlib import Path

from split_settings.tools import include

BASE_DIR = Path(__file__).resolve().parent.parent

WSGI_APPLICATION = 'core.wsgi.application'
include("components/*.py")
