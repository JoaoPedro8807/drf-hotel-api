
from django.conf import settings
from .models import Booking
from celery import shared_task
from celery.utils.log import get_task_logger
from .models import Booking
from django.core.exceptions import ObjectDoesNotExist
from .services import att_available_room
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime

 
logger = get_task_logger(__name__)
 
@shared_task()
def thirty_second_func(): #testando
    logger.info("I run every 30 seconds using Celery Beat")
    return "Done"
 

@shared_task(bind=True) 
def booking_att_task(self, *args, **kwargs):    
    """
    schedule task to atualizate booking, room, and send email finalization to celery worker
    """
    request_data = kwargs.get('request_data')
    user_data = kwargs.get('user_data')
    booking_id = str(request_data.get('id'))
    room_id = str(request_data.get('room'))
    try:
        booking = Booking.objects.get(id=booking_id)    
        booking.delete()

        send_email_finalization_booking(**user_data, booking_data=request_data)
        att_available_room(room_id=room_id, status=True)
        print(f'booking com id {booking_id}, deletado, e room {room_id} atualizada')

    except (ObjectDoesNotExist, Exception) as e:
        print('erro no booking_att_task: ', str(e))
        
        
    return "Done"   


@shared_task
def send_email_booking_confirmation_task(email, user_name, room_detail, price, end_date):
    """
    simple task to send booking email confirmation to celery worker
    """
    subject = "Booking Confirmation"
    from_email = 'projecthoteproject@gmail.com'
    to_email = [email]
    context = {
        'user_name': user_name,
        'room_detail': room_detail,
        'price': price,
        'end_date': end_date,
        'current_year': datetime.now().year,
    }

    html_content = render_to_string('email_confirmation.html', context)
    text_content = strip_tags(html_content)

    email_msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email_msg.attach_alternative(html_content, "text/html")
    email_msg.send()
    print(f'Email para {email} enviado com sucesso')
    return "Done"

   
@shared_task
def send_email_finalization_booking(email: str, username: str, booking_data):
    """
    simple task to send finalization booking email to celery worker
    """
    subject = "Booking Finalization"
    from_email = 'projecthoteproject@gmail.com'
    to_email = [email]
    context = {
        'user_name': username,
        'booking_data': booking_data,
        'current_year': datetime.now().year,
    }

    html_content = render_to_string('email_finalization.html', context)
    text_content = strip_tags(html_content)

    email_msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email_msg.attach_alternative(html_content, "text/html")
    email_msg.send()