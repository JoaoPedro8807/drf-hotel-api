from rest_framework import serializers
from hotelier.models import HotelierUser
from hotel.serializers import HotelRelatedDetailSerializer
from guests.serializers.auth.user_auth_serializer import UserAuthInfoSerializer

class HotelierProfileSerializer(serializers.ModelSerializer):
    hotel = HotelRelatedDetailSerializer(read_only=True)
    auth_user = UserAuthInfoSerializer(read_only=True)
    class Meta:
        model = HotelierUser
        fields = [
            'auth_user',
            'hotelier_id',
            'document', 
            'phone_number', 
            'first_name',
            'last_name',
            'hotel'
            ]
        

    hotelier_id = serializers.UUIDField(
        source='id',
        read_only=True
    )
    
