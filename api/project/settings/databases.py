import os
from dotenv import load_dotenv
from pathlib import Path
from project.settings.assets import ENV_DIR
load_dotenv(ENV_DIR)

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', ''),
        'NAME': os.environ.get('POSTGRES_DB', ''),
        'USER': os.environ.get('POSTGRES_USER', ''),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'HOST': os.environ.get('POSTGRES_HOST', ''),
        'PORT': os.environ.get('POSTGRES_PORT', '')
    }
}

