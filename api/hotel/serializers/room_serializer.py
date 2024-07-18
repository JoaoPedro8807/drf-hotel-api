from rest_framework import serializers
from ..models.hotel_model import Hotel
from ..models.room_model import Room
from ..validators.room_validator import RoomValidatorEntry

class RoomSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='hotel:room-detail',  
        lookup_field='id',
        read_only=True,
    )    
    class Meta:
        model = Room
        fields = [
            'hotel',
            'id',
            'room_number',
            'room_type',  
            'room_description',  
            'bed_count',
            'daily_price',
            'available',
            'detail',
            'hotel',
            'image',
            'andress',
            ]
    andress = serializers.SerializerMethodField(
        method_name='get_hotel_andress'                                                             
    )
    image = serializers.ImageField(write_only=True, required=False) #image just show in detail

    def get_hotel_andress(self, instance):
        return f'{instance.hotel.street} ({instance.hotel.zip_code}). {instance.hotel.city} - {instance.hotel.state}'
    
    def validate(self, attrs):
        RoomValidatorEntry(data=attrs)
        return super().validate(attrs)


class RoomDetailSerializer(serializers.ModelSerializer):

    hotel = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Room
        fields = [
            'id',
            'room_number',
            'room_type',
            'daily_price',
            'available',
            'bed_count',
            'room_description',
            'image',
            'hotel',
        ]


    