from rest_framework import serializers
from ..models.hotel_model import Hotel
from ..models.room_model import Room
from ..serializers.room_serializer import RoomSerializer

class HotelSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = [
            'hotel_id',
            'total_rooms',
            'stars_class',
            'available_rooms',
            'hotelier',
            'name',
            'street',
            'city',
            'state',
            'zip_code',     
            'hotel_description',
            'rating',
            'rooms',
            ]

    hotel_id = serializers.UUIDField(
        source='id',
        read_only=True
    )   
                                                                        
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation
    
    def validate(self, attrs):
        return super().validate(attrs)

        