from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework.validators import ValidationError
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
import re

class UserHotelierManager(models.Manager):
     def create_hotelier(
            self,
            auth_user,
            document: str,
            phone_number: str,
            first_name: str,
            last_name:str,
            ):
        hotelier = self.model(
            auth_user=auth_user,
            document=document,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            ) 
        return hotelier
