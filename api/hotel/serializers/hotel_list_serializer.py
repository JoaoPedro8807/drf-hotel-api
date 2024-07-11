from rest_framework import serializers
from ..models import Hotel
from ..models import Room
from ..serializers.room_serializer import RoomSerializer
class HoteListSerializer(serializers.HyperlinkedModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='hotel:detail_hotel-detail',  
        lookup_field='id'
    )
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'total_rooms', 'stars_class', 'available_rooms', 'detail']
    


class HotelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = [
            'id',
            'created_at',
            'name',
            'total_rooms',
            'stars_class',
            'total_available_rooms',
        ]

    total_available_rooms = serializers.IntegerField(
        source='available_rooms'
    )

    def get_available_rooms_data(self):
        rooms = Room.objects.filter(
            hotel=self.instance,
            available=True
        )
        return RoomSerializer(instance=rooms, many=True).data
    
    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['available_rooms'] = self.get_available_rooms_data()

        return representation
        