from rest_framework.request import Request
from ..serializers.user_token_login_serializer import LoginTokenSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from django.utils import timezone
User = get_user_model()


class LoginView(TokenObtainPairView):
    serializer_class = LoginTokenSerializer

    def update_last_login(self, user):
        user.last_login = timezone.now()
        user.save()
        

    def post(self, request: Request, *args, **kwargs) -> Response:
        response = super().post(request, *args, **kwargs) #response from TokenObtainPariSerializer, that resopnse return 200 if login is ok
        if response.status_code == status.HTTP_200_OK:
            print('RESPONSE OK')
            try:
                user = User.objects.filter(email=request.data.get('email')).first()
                self.update_last_login(user=user)

            except Exception as e:
                print(f'erro ao logar {e}')

        return response





