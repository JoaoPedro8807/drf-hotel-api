from rest_framework import serializers
from hotelier.models import HotelierUser
from ..validators.hotelier_entry_validator import HotelEntryValidator
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
    
    def validate(self, attrs):
        HotelEntryValidator(data=attrs)
        return super().validate(attrs)

    hotelier_id = serializers.UUIDField(
        source='id',
        read_only=True
    )
    
