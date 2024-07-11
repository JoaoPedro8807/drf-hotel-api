from rest_framework import serializers
from ..models.hotel_model import Hotel
from ..models.room_model import Room
from .hotel_detail_serializer import HotelRelatedDetailSerializer
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'room_number',
            'room_type',
            'daily_price',
            'available'
            ]
        

class RoomDetailSerializer(serializers.ModelSerializer):
    hotel = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Room
        fields = [
            'room_number',
            'room_type',
            'daily_price',
            'hotel'
        ]

    def to_representation(self, instance):
        repesentation = super().to_representation(instance)        
        return repesentation

    