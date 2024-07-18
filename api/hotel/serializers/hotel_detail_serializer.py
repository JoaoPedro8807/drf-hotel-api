from rest_framework import serializers
from ..models.hotel_model import Hotel
from . import RoomDetailSerializer

class HotelRelatedDetailSerializer(serializers.ModelSerializer):
    rooms = RoomDetailSerializer(many=True)
    class Meta:
        model = Hotel
        fields = [
            'id',
            'stars_class',
            'name',     
            'street',
            'city',
            'state',
            'zip_code',
            'hotel_description',
            'rating',
            'rooms'                                                                
            ]

