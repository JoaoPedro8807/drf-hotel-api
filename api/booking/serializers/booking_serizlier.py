from rest_framework import serializers
from ..models import Booking
from ..validators import BookingEntryValidator
from hotel.serializers import RoomDetailSerializer, RoomSerializer
from hotel.serializers import HoteListSerializer

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id',
            'start_date',
            'end_date',
            'days',
            'guest',
            'room',
            'price',
            ]
    id = serializers.UUIDField(
        read_only=True
    )
    
    def validate(self, attrs):
        validate =  super().validate(attrs)
        BookingEntryValidator(
            data=attrs
        )
        return validate 


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['room_detail'] = RoomDetailSerializer(instance=instance.room).data
        representation['hotel_detail'] = HoteListSerializer( #show only hotel basic infos
            instance=instance.room.hotel, 
            read_only=True, context={'request': self.context.get('request')}).data

        return representation

class BookingInfoSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = [
            'id',
            'start_date',
            'end_date',
            'days',
            'price',
            'room',
            ]