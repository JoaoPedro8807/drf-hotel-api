from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .abstract_model import AbstractHotelModel
from .managers.rooms_manager import RoomManager

class Room(AbstractHotelModel):# colocar model normal qualquer coisa se der erro.
    hotel = models.ForeignKey("hotel.Hotel", verbose_name=_("hotel"), on_delete=models.CASCADE, related_name='rooms')    
    room_number = models.PositiveIntegerField(_("room number"))
    room_type = models.CharField(_("room type"), choices={('S', 'SINGLE'), ('D', 'DOUBLE'), ('T', 'TRIPLE')}, max_length=2)
    daily_price = models.DecimalField(_("daily price"), max_digits=10, decimal_places=2)
    available =  models.BooleanField(_("available"), default=True)

    class Meta:
        verbose_name = _("room")
        verbose_name_plural = _("rooms")
        db_table = 'room'

    objects = RoomManager()
    
    
    def __str__(self) -> str:
        return f'Quarto {self.room_number} do hotel {self.hotel}'       