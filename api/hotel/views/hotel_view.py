from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination 
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from rest_framework import status
from ..permissions import  IsHotelOwner
from ..models.hotel_model import Hotel
from ..serializers.hotel_serialize import HotelSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated



class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'
    lookup_value_regex = r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"
    http_method_names = ['get', 'post', 'patch', 'delete']
    

    def get_object(self):
        uuid = self.kwargs.get('uuid', '')  
        print('UUID QUE VEM DO TEST NA VIEWSET: ', uuid)
        hotel = get_object_or_404(  
            self.get_queryset(),
            id=uuid
        )
        self.check_object_permissions(request=self.request, obj=hotel)
        return hotel

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(),]
        
        return [IsHotelOwner(), ]
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs): 
        if 'uuid' not in request.query_params:  #just get the own hotel
            return Response(
                {"detail": "Ação não permitida"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().list(request, *args, **kwargs)
    