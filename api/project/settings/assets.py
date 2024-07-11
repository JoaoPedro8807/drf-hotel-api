from .enviroment import BASE_DIR, DATA_DIR
from pathlib import Path
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
ENV_DIR = BASE_DIR / 'dotenv_files' / '.env'


STATIC_URL = '/static/'

STATIC_ROOT = DATA_DIR / 'static'

STATICFILES_DIRS = [
    BASE_DIR / 'base_static',
]

MEDIA_URL = '/media/'

MEDIA_ROOT = DATA_DIR / 'media'