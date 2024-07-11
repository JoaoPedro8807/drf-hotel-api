from rest_framework import serializers
from ..models.hotel_model import Hotel

class HotelRelatedDetailSerializer(serializers.ModelSerializer):
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
            ]