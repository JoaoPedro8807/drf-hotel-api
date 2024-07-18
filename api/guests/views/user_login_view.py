from rest_framework.request import Request
from ..serializers.auth.user_token_login_serializer import LoginTokenSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from django.utils import timezone
User = get_user_model()


class LoginView(TokenObtainPairView):
    """
        Endpoint to make login and take the access token
    """
    serializer_class = LoginTokenSerializer

        
    def get_queryset(self):
        return User.objects.select_related('hotelier_user', 'guest_user')        






