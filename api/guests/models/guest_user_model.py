from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework.validators import ValidationError
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
import re
from .abstract_model import BaseAbstractModel
from hotel.models.abstract_model import AbstractHotelModel


class UserGuestManager(models.Manager):
     def create_guest(
            self,
            auth_user,
            document: str,
            phone_number: str,
            first_name: str,
            last_name:str,
            ):
        guest = self.model(
            auth_user=auth_user,
            document=document,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            ) 
        return guest


class UserGuest(AbstractHotelModel):  
    auth_user = models.OneToOneField("guests.UserAuth", verbose_name=_("guest_user"), on_delete=models.CASCADE, related_name='guest_user')
    document = models.CharField(_("CPF"), max_length=50, unique=True)     #Guest and Hotelier use a different type of document  s
    birthday = models.DateField(_("user birthday"), default=timezone.now, blank=True, null=True) 
    phone_number = models.CharField(_("phone number"), max_length=20, blank=True)
    first_name = models.CharField(_("first name"), max_length=50, blank=True)
    last_name = models.CharField(_("last name"), max_length=50, blank=True)      
    
    objects = UserGuestManager()

    class Meta:
        verbose_name = _("guest user")
        verbose_name_plural = _("guest user ")
        db_table = "user_guest"

    def clean(self) -> None:
        return super().clean()

    def save(self, *args, **kwargs):
        sp = super().save(*args, **kwargs)
        print('FIELD DO SAVE: ', self.auth_user)
        return sp