from collections import defaultdict
from django.contrib.auth import get_user_model 
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from ..validators import UserAuthValidator



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [                                  
            'uuid', 
            'username',
            'email',
            'created_at',
            'is_staff', 
            'type_user',
            'type_user',
            'last_login',
            'user_id',
            'user_info'
            # ---------> Fazer campo para juntar as infos do guest ou hotelier <-----------------
        ]
    user_id = serializers.UUIDField(
        source='uuid',
        read_only=True
    )
    user_info = serializers.SerializerMethodField(
        read_only=True,
        method_name='get_user_info',
    )


    def get_user_info(self, user_object):
        if user_object.type_user == 'GS':
            return self.get_guest_infos(user_object)
        
        return self.get_hotelier_infos(user_object)
    

    def get_guest_infos(self, user): #get all guests infos (books, locales, etc..s)
        return {
            'guest': 'guest'
        }
        ...

    def get_hotelier_infos(self, user): #get all hotelier infos (books, hotel_locals, hotel_infos, rooms,  etc...)
        return 'hotelier'
        ...