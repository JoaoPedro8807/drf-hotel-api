from .test_user_api import *
from .test_user_create import *
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()  