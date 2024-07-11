from django.contrib.auth import get_user_model
from ..models.guest_user_model import UserGuest
from ..models.user_auth_model import UserAuth
from hotelier.models.hotelier_user_model import HotelierUser
from .user_guest_serializer import GuestUserSerializer
from hotelier.serializers.hotelier_serializer import HotelierSerializer

def serializer_especific(user: UserAuth):
    especific_user = user.especific_user
    
    if isinstance(especific_user, UserGuest):
        return GuestUserSerializer(especific_user).data

    elif isinstance(especific_user, HotelierUser):
        return HotelierSerializer(especific_user).data
    print('NO TESTE NENHUM DOS DOIS')
    return None
