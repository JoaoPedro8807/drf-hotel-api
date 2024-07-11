# Importações necessárias
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models.hotel_model import Hotel
from ..models.room_model import Room

@receiver(post_save, sender=Hotel)
def create_hotel_rooms(sender, instance, created, **kwargs):
    if created:
        ...
