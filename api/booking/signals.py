# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking
from .tasks import send_email_booking_confirmation_task as send_email_task, booking_att_task
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from .serializers.booking_serizlier import  BookingSerializer
from .services import att_available_room

@receiver(post_save, sender=Booking)
def update_room_status(sender, instance, created, **kwargs):
    if created:
        try:
            room = instance.room
            room.available = False
            room.save()
            
        except (Exception, ObjectDoesNotExist) as error:
            print('erro  ao mudar o status: ', error)

@receiver(post_save, sender=Booking)
def send_booking_confirmation_email_task(sender, instance, created, **kwargs):
    if created:
        msg_data = BookingSerializer(instance=instance).data 
        send_email_task.delay(
            email=instance.guest.auth_user.email, 
            user_name = instance.guest.auth_user.username,
            room_detail=msg_data.get("room_detail"),
            price=float(instance.price),
            end_date = str(instance.end_date)
            )

@receiver(post_save, sender=Booking)    
def att_booking_celery_task(sender, instance, created, **kwargs):
    if created:
        days = instance.days
        ETA = (datetime.now() + timedelta(days=days)).replace(second=0, microsecond=0) 
        data = BookingSerializer(instance=instance).data
        booking_att_task.apply_async(
            kwargs={'request_data': data},
            eta=ETA
        )

