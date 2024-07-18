from django.db import models
from .abstract_booking_model import AbstractHotelModel
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta
from django.utils.timezone import now
from rest_framework.validators import ValidationError
from datetime import datetime

class Booking(AbstractHotelModel):
    start_date = models.DateField(auto_now_add=True, editable=False)  
    end_date = models.DateField(blank=True, null=True)      
    days = models.PositiveIntegerField(_('days'))
    guest = models.OneToOneField("guests.UserGuest", verbose_name=_("guest"), on_delete=models.CASCADE, related_name='booking')
    room = models.OneToOneField("hotel.Room", verbose_name=_("room"), on_delete=models.CASCADE, related_name='room')
    status = models.BooleanField(_("status"), default=True)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = _("booking")
        verbose_name_plural = _("bookings")
        db_table = 'booking'

    def save(self, *args, **kwargs):
        self.price = round((self.room.daily_price * self.days), 2)

        if not self.days:
            self.days = 1
        self.end_date = datetime.now().date() + timedelta(days=self.days)

        if Booking.objects.filter(
            start_date=datetime.now().date(), 
            end_date=self.end_date, room=self.room).exists():
                raise ValidationError({'date': f'A booking with {self.start_date} for this room already exist'})            
        
        return super().save(*args, **kwargs)