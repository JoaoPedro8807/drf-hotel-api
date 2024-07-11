from hotel.tests.base.hotel_mixins import HotelMixin
from guests.tests.mixins.user_mixins import UserAPIMixin
from django.urls import reverse
import json

class BookingTestMixin(HotelMixin, UserAPIMixin):
    def make_all_booking_data(
        self,
        guest_email: str = 'testandoboking@gmail.com',
        guest_password: str = 'Testandobooking123!',
        total_days: int = 5,
        all_data = False
    ) -> dict:
        hotel = self.make_login_and_hotel().get('create_response')
        room_to_booking = hotel.data.get('rooms')[0]

        guest_data = self.make_user_data(
            email=guest_email, 
            password = guest_password)
        
        guest_user = self.client.post(
            self.urls.get('create_user'),
            data={**guest_data}
        )        
        guest_login = self.client.post(
            reverse('guests:login'),
            data={
                'email': guest_email,
                'password': guest_password
            })
        
        guest_id = guest_login.data.get('user_info').get('guest_id')
        access_token = guest_login.data.get('access')
  
        post_data = {
            'guest': str(guest_id),
            'room': room_to_booking.get('id'),
            'days': int(total_days)
        }   
        booking_response = self.client.post(
            reverse('booking:booking_viewset-list'),
            content_type='Application/json',
            data=json.dumps(post_data),
            HTTP_AUTHORIZATION = f'Bearer {access_token}'
        )
        if all_data:
            return {
                'hotel': hotel,
                'room': room_to_booking,
                'guest_data': guest_data,
                'guest_login': guest_login,
                'booking_response': booking_response
            }
        return booking_response 
    

    def make_all_hotel_data(self):
        login_hotelier = self.make_login_hotelier()
        hotelier = login_hotelier.data.get('user_info').get('hotelier_id')
        hotel = self.make_hotel(hotelier_user=hotelier, access_token=login_hotelier.data.get('access'))
        return hotel, login_hotelier, hotelier
    
    def make_room_to_booking(self):
        hotel = self.make_login_and_hotel().get('create_response')
        room_to_booking = hotel.data.get('rooms')[0]
        return room_to_booking

    def make_only_booking(self, guest_id, access, room_id, total_days=5):
        post_data = {
            'guest': str(guest_id),
            'room': str(room_id),
            'days': total_days
        }   

        booking_response = self.client.post(
            reverse('booking:booking_viewset-list'),
            content_type='Application/json',
            data=json.dumps(post_data),
            HTTP_AUTHORIZATION = f'Bearer {access}'
        )
        return booking_response
    
    def make_all_guest_data(
            self, 
            guest_email = 'testandobooking@gmail.com', 
            guest_password='Testandobooking123!',
            extra_data = {}
            ):
        
        guest_data = self.make_user_data(
            email=guest_email, 
            password = guest_password,
            **extra_data
            )
        
        auth = self.client.post(
            self.urls.get('create_user'),
            data={**guest_data}
        )        
        guest_login = self.client.post(
            reverse('guests:login'),
            data={
                'email': guest_email,
                'password': guest_password
            })
        return guest_login, auth