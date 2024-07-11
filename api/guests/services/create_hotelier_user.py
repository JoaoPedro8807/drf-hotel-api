from ..models.user_auth_model import UserAuth
from hotelier.models.hotelier_user_model import HotelierUser
from django.core.exceptions import ValidationError
from django.db import IntegrityError, OperationalError
from django.db import transaction


def create_hotelier_user(auth_user: UserAuth, fields: dict):
    hotelier = HotelierUser.objects.create_hotelier( 
        auth_user=auth_user,
        document=fields.get('document', ''),
        phone_number=fields.get('phone_number', ''),
        first_name=fields.get('first_name', ''),
        last_name=fields.get('last_name', '')
    )
    hotelier.full_clean()
    hotelier.save()
    return hotelier
        
        