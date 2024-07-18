from rest_framework.response import Response
from rest_framework.validators import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..permissions import  IsHotelOwner
from ..models.hotel_model import Hotel
from ..serializers.hotel_serialize import HotelSerializer
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

class HotelViewSet(
    viewsets.GenericViewSet, 
    viewsets.mixins.DestroyModelMixin,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.UpdateModelMixin
    ):
    """
        CRUD a hotel, nedded be logged as Hotelier, then can edit your Hotel instance.
    """
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'
    lookup_value_regex = r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"
    http_method_names = ['post', 'patch', 'delete']
    

    def get_object(self):
        uuid = self.kwargs.get('uuid', '')  
        hotel = get_object_or_404(  
            self.get_queryset(),
            id=uuid
        )
        self.check_object_permissions(request=self.request, obj=hotel)
        return hotel
    
    def create(self, request, *args, **kwargs):
        try:
            hotel_data = HotelSerializer(data=request.data)
            hotel_data.is_valid(raise_exception=True)
            create_data = hotel_data.data
            create_data['hotelier'] = self.request.user.hotelier_user
            create_data['total_rooms'] = 0
            print('DATA PRO CREATE', create_data)
            hotel = Hotel.objects.create(**create_data)
            reponse_data = HotelSerializer(hotel).data            

            return Response(reponse_data, status=status.HTTP_201_CREATED)
        
        except (IntegrityError, ObjectDoesNotExist) as error:
            return Response({'error': f'Erro ao criar o hotel, {str(error)}, tente novamente!'})
        
        except Exception as error:
            raise ValidationError(error)


    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(),]
        
        return [IsHotelOwner(), ]
    

