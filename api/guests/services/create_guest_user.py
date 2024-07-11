from ..models.guest_user_model import UserGuest
from rest_framework.validators import ValidationError
from django.db import IntegrityError, OperationalError
from rest_framework.exceptions import ValidationError as DRFValidationError


def create_guest(auth_user, fields):
    guest = UserGuest.objects.create_guest(
        auth_user=auth_user,
        document=fields.get('document', ''),
        phone_number=fields.get('phone_number', ''),
        first_name=fields.get('first_name',''),
        last_name=fields.get('last_name', '')
    )
    guest.full_clean()
    guest.save()
    return guest
    
    