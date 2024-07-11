from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework.validators import ValidationError
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
import re

class HotelManager(models.Manager):
    ...