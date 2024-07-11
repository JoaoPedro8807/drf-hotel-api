from django.contrib.auth import get_user_model 
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models.guest_user_model import UserGuest
from hotelier.models.hotelier_user_model import HotelierUser
from ..validators import UserAuthValidator
from .user_guest_serializer import GuestUserSerializer
from hotelier.serializers.hotelier_serializer import HotelierSerializer


User = get_user_model()

class UserAuthSerializer(ModelSerializer):
    class Meta: 
        model = User
        fields = [      
            'user_id',                         
            'username',
            'email',
            'password',
            'created_at',
            'is_staff', 
            'type_user',
            'user_id',
            'auth_info',
        ]
      
    user_id = serializers.UUIDField(
        source='uuid',
        read_only=True
    )
    auth_info = serializers.SerializerMethodField(
         method_name='get_auth_info',
     )

    password = serializers.CharField(
        write_only=True
    )

    def get_auth_info(self, user_object):
        return{
            'staff': user_object.is_staff,
            'last_login': user_object.last_login,
            }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        especific_user = instance.especific_user
        if isinstance(especific_user, UserGuest):
            representation['user_info'] = GuestUserSerializer(especific_user).data
        elif isinstance(especific_user, HotelierUser):
            representation['user_info'] = HotelierSerializer(especific_user).data
        
        return representation    
    
    def validate(self, attrs):
        sp = super().validate(attrs)
        if self.context['request'].method.upper() == 'PATCH': #In partial update, the seriliazer and model check for each field, not validators
            return sp 
        
        UserAuthValidator(
            data=attrs,
            ErrorClass=serializers.ValidationError, 
        )
        return sp
    

                   

            
        
    

        

    