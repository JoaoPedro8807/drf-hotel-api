from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..permissions import  IsHotelOwner
from ..models.hotel_model import Hotel
from ..serializers.hotel_serialize import HotelSerializer
from rest_framework.permissions import IsAuthenticated
from ..serializers import RoomSerializer
from ..models import Room
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

class RoomViewSet(viewsets.ModelViewSet):
    """
        CRUD a ROOM, nedded be logged as Hotelier, then can edit your Hotel instance.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'
    lookup_value_regex = r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"
    http_method_names = ['post', 'patch', 'delete']


    def get_object(self):
        id =self.kwargs.get('uuid')
        hotel = get_object_or_404(  
            self.get_queryset(),
            hotel__hotelier=self.request.user.hotelier_user,
            id=id
        )
        self.check_object_permissions(request=self.request, obj=hotel)
        return hotel
     
    def create(self, request, *args, **kwargs):
        available_data = request.data.get('available', None)
        if available_data is None:
            request.data['available'] = True #the default is true

        create = super().create(request, *args, **kwargs)
        print('DEPOIS: ', create.data)
        if create.status_code == status.HTTP_201_CREATED:
            try:
                room_id = create.data.get('id')
                objt = Room.objects.filter(id=room_id).first()
                objt.hotel.total_rooms += 1
                objt.hotel.available_rooms += 1
                objt.hotel.save()

            except (ObjectDoesNotExist, IntegrityError) as error:
                return Response({'error': f'Erro ao atualizar o hotel, {str(error)}, tente novamente'}, status=status.HTTP_400_BAD_REQUEST)
        return create