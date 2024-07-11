from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.admin.models import LogEntry

User = get_user_model()

class TesteSerializerCrl(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name']


class TesteViewSetCrl(viewsets.ModelViewSet):   
    queryset = User.objects.all()
    serializer_class = TesteSerializerCrl
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post', 'patch', 'post', 'delete', 'options', 'head' ] 

    