from rest_framework import serializers
from ..models import UserGuest
from ..validators import UserGuestValidator
class GuestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGuest
        fields = ['document', 'phone_number', 'first_name', 'last_name', 'guest_id']

    guest_id = serializers.UUIDField(
        source='id',
        read_only=True
    )
        # Adicione outros campos necessários do modelo GuestUser        

    def validate(self, attrs):
        validate = super().validate(attrs)
        
        UserGuestValidator(
            data=attrs
        )
        return validate

        