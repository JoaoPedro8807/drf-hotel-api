from collections import defaultdict
from django.contrib.auth import get_user_model 
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from ..validators import UserAuthValidator
from ..models.guest_user_model import UserGuest
from ..serializers.auth.user_auth_serializer import UserAuthInfoSerializer
from booking.serializers.booking_serizlier import BookingInfoSerializer


class ProfileSerializer(serializers.ModelSerializer):
    auth_user = UserAuthInfoSerializer(read_only=True)
    booking = BookingInfoSerializer(read_only=True)
    class Meta:
        model = UserGuest
        fields = [                                  
            'auth_user',
            'guest_id',
            'phone_number',
            'first_name',
            'last_name',
            'booking'
        ]
    guest_id = serializers.UUIDField(
        source='id',
        read_only=True
    )


   