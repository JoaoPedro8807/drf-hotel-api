from rest_framework.viewsets import ReadOnlyModelViewSet
from ..serializers.profile_serializer import ProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

User = get_user_model()

class UserProfileViewSet(ReadOnlyModelViewSet): #viewset só com get, muito menos permissiva
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return User.objects.filter(email=self.request.user.email)

    @action( #decorator que faz o método virar um endpoint. 
            methods=['GET',],
            detail=False
    )
    def me(self, request, *args, **kwargs): #método para mostrar o perfil do user
        obj = self.get_queryset().first() #como n temos pk aqui no request, podemos pegar o obj com o username que já está no queryset da class e dar um .first()
        serializer = self.get_serializer(
            instance=obj
        )
        return Response(
            serializer.data
        )