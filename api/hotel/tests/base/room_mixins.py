from .hotel_mixins import HotelMixin
from django.urls import reverse
import json

class RoomMixin(HotelMixin):
    def make_room_and_hotel(
            self, 
            hotel = None,
            room_number:int = 1,
            room_type: str = 'S',
            daily_price: float = 100.0,
            bed_count: int = 1
            ):
        hotel_response = self.make_login_and_hotel()
        hotel_create = hotel_response.get('create_response')
        hotel_login = hotel_response.get('login_response')
        
        print('CREATE_RESPONSE: ', hotel_create.data)
        hotel_id = hotel_create.data.get('hotel_id')
        jwt_access = hotel_login.data.get('access')

        post_data = {
            'hotel': str(hotel_id),
            'room_number': room_number,
            'room_type': room_type,
            'daily_price': daily_price,
            'bed_count': bed_count
        }

        return self.client.post(
            reverse('hotel:room_viewset-list'),
            data=json.dumps(post_data),
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer {jwt_access}'
        )

         