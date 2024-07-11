import os
from pathlib import Path
from utils.get_env_vars import parse_comma_sep_str_to_list, get_env_variable

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR.parent / 'data' / 'web'

SECRET_KEY = os.environ.get('SECRET_KEY', 'INSECURE')
SECRET_KEY_JWT = os.environ.get('SECRET_KEY_JWT')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if int(os.environ.get('DEBUG', 1)) == 1 else False

ALLOWED_HOSTS: list[str] = parse_comma_sep_str_to_list(
    get_env_variable('ALLOWED_HOST')
)
CSRF_TRUSTED_ORIGINS = parse_comma_sep_str_to_list(
    get_env_variable('CSRF_TRUSTED_ORIGINS')
)
print('CSRF : ', CSRF_TRUSTED_ORIGINS)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "guests.UserAuth"