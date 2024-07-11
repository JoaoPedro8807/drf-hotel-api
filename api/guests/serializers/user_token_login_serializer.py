from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .especific_user_serializer import serializer_especific
from .user_serializer import  UserAuthSerializer

class LoginTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user_infos = {
            'user_info': serializer_especific(self.user)
        }
        user_infos.update(UserAuthSerializer(self.user).data)
       
        data.update(user_infos)
        return data
