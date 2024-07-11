from rest_framework import serializers
from hotelier.models import HotelierUser
class HotelierSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelierUser
        fields = [
            'hotelier_id',
            'document', 
            'phone_number', 
            'first_name',
            'last_name'
            ]
        

    hotelier_id = serializers.UUIDField(
        source='id',
        read_only=True
    )
    
