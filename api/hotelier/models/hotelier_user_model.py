from django.contrib.auth import get_user_model 
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from hotel.models.abstract_model import AbstractHospedagemModel
from .managers.hotelier_user_manager import UserHotelierManager


class HotelierUser(AbstractHospedagemModel): 
    auth_user = models.OneToOneField("guests.UserAuth", verbose_name=_("hotelier user"), on_delete=models.CASCADE, related_name='hotelier_user')
    document = models.CharField(_("CNPJ"), max_length=50, unique=True)     #Guest and Hotelier use a different type of documents
    phone_number = models.CharField(_("phone number"), max_length=20, blank=True)
    first_name = models.CharField(_("first name"), max_length=50, blank=True)
    last_name = models.CharField(_("last name"), max_length=50, blank=True)      
                                                                            
    objects = UserHotelierManager()                         


    class Meta:
        verbose_name = _("hotelier")                                                                                    
        verbose_name_plural = _("hoteliers")
        db_table = 'hotelier'    
