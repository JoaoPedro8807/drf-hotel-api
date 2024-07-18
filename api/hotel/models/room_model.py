from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .abstract_model import AbstractHospedagemModel
from .managers.rooms_manager import RoomManager
import os

def room_image_upload_path(instance, filename):
    return os.path.join(f'rooms/images/{str(instance.hotel)}/{instance.room_number}', str(instance.id), filename) #hotel.name has a unique constrait

class Room(AbstractHospedagemModel):
    hotel = models.ForeignKey("hotel.Hotel", verbose_name=_("hotel"), on_delete=models.CASCADE, related_name='rooms')    
    room_number = models.PositiveIntegerField(_("room number"))
    room_description = models.TextField(max_length=255, null=True, blank=True)
    room_type = models.CharField(_("room type"), choices={('S', 'SINGLE'), ('D', 'DOUBLE'), ('T', 'TRIPLE')}, max_length=1)
    daily_price = models.DecimalField(_("daily price"), max_digits=10, decimal_places=2)
    available =  models.BooleanField(_("available"), default=True)
    bed_count = models.PositiveIntegerField(_("number of bed in room"), blank=True, default=1)
    image = models.ImageField(upload_to=room_image_upload_path, blank=True, null=True)
    
    class Meta: 
        verbose_name = _("room")    
        verbose_name_plural = _("rooms")
        db_table = 'room'

    objects = RoomManager()

    
    
    def __str__(self) -> str:
        return f'Room {self.room_number} from {self.hotel} hotel'       