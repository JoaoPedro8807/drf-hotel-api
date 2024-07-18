from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .abstract_model import AbstractHospedagemModel
from .managers.hotel_manager import HotelManager

class Hotel(AbstractHospedagemModel):
    hotelier = models.OneToOneField("hotelier.HotelierUser", verbose_name=_("hotelier"), on_delete=models.CASCADE, related_name='hotel')
    name = models.CharField(max_length=50, unique=True)
    total_rooms = models.PositiveIntegerField(_("numbers of rooms" ), blank=True)
    hotel_description = models.CharField(max_length=255, blank=True, null=True)
    stars_class = models.IntegerField(_("number of stars"))
    rating = models.FloatField(_("number of rating"), default=1)    
    available_rooms = models.PositiveIntegerField(_("number of available rooms"), default=0)
    street = models.CharField(_("hotel street"), max_length=255, blank=True, null=True)
    city = models.CharField(_("hotel city"), max_length=100, blank=True, null=True)
    state = models.CharField(_("hotel state"), max_length=100, blank=True, null=True)
    zip_code = models.CharField(_("hotel zip code"), max_length=10, blank=True, null=True)
    
    
    objects = HotelManager()


    class Meta:
        verbose_name = _("hotel")
        verbose_name_plural = _("hoteis")
        db_table = 'hotel'
        


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
