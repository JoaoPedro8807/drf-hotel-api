from rest_framework import serializers
from ..models.hotel_model import Hotel
from ..models.room_model import Room
from ..serializers.room_serializer import RoomSerializer

class HotelSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True)

    class Meta:
        model = Hotel
        fields = [
            'hotel_id',
            'total_rooms',
            'stars_class',
            'available_rooms',
            'hotelier',
            'name',     
            'rooms',
            ]

    hotel_id = serializers.UUIDField(
        source='id',
        read_only=True
    )   
    
    def create(self, validated_data):
        rooms_data = validated_data.pop('rooms')
        hotel = Hotel.objects.create(**validated_data)
        
        for room_data in rooms_data:
            Room.objects.create(hotel=hotel, **room_data)

        hotel.total_rooms = len(rooms_data)
        hotel.available_rooms = len(rooms_data)
        hotel.save()

        return hotel


    def update(self, instance, validated_data):
        rooms_data = validated_data.pop('rooms', [])
        instance = super().update(instance, validated_data)
        
        for room_data in rooms_data:
            room_number = room_data.get('room_number')
                # Update existing room
            try:
                room_instance = Room.objects.get(room_number=room_number, hotel=instance)
                print('room att no serializer: ', room_instance)
                room_update = RoomSerializer().update(room_instance, room_data)
                room_update.save()

            except Room.DoesNotExist:
                continue  
    
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation
    

        