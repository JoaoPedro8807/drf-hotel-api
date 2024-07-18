from collections import defaultdict
from rest_framework.validators import ValidationError
class RoomValidatorEntry:
    def __init__(self, data):
         self.errors = defaultdict(list)
         self.data = data
         self.clean()
        

    def clean(self):
        self.clean_price()
        if self.errors:
            raise ValidationError(self.errors)

    def clean_price(self):
        daily_price = self.data.get('daily_price')
        try:
            daily_price = float(daily_price)

        except (ValueError, TypeError):
            self.errors['daily_price'].append('Daily price must be a valid number.')
            return

        if daily_price <= 0.0:
            self.errors['price'].append(f'The price {daily_price} must be positive.')

    def clean_type_room(self):
        room_type = self.data.get('room_type').upper()
        types = [('S', 'SINGLE'), ('D', 'DOUBLE'), ('T', 'TRIPLE')]
        if not room_type in types:
            self.errors['room_type'].append(f'room type {room_type} dont meet the  type requirements: {types}')