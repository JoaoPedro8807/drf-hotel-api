from .base.booking_base_test import BookingTestBase
from django.urls import reverse
import json
from rest_framework import status
from unittest.mock import patch
from hotel.models import Room
from ..models import Booking
from datetime import datetime, timedelta
from rest_framework.validators import ValidationError
from .base import BookingEditMixin

class BookingEditTest(BookingTestBase, BookingEditMixin):
    def test_guest_can_delete_own_booking(self):
        guest_login, _ = self.make_all_guest_data()
        guest_id = guest_login.data.get('user_info').get('guest_id')
        access = guest_login.data.get('access')

        room = self.make_room_and_hotel()
        room_id = str(room.data.get('id'))

        booking = self.make_only_booking(
            guest_id=guest_id,
            access=access,
            room_id=room_id,
            total_days=5
        )         
        booking_id = booking.data.get('id')
        delete = self.delete_booking(booking_id=booking_id, access=access)

        self.assertEqual(delete.status_code, status.HTTP_204_NO_CONTENT)



    def test_return_error_when_user_try_delete_or_get_other_booking(self):
        guest1, _ = self.make_all_guest_data()
        guest1_id = guest1.data.get('user_info').get('guest_id')    
        access_1 = guest1.data.get('access')

        guest2, _ = self.make_all_guest_data(
            guest_email='guest2testando@gmail.com', 
            extra_data={'document': '132131232132131'}) #without unique constraints
        guest2_id = guest2.data.get('user_info').get('guest_id')
        access_2 = guest2.data.get('access')

        room = self.make_room_and_hotel()
        room_id = str(room.data.get('id'))

        booking = self.make_only_booking(
            guest_id=guest1_id,
            access=access_1,
            room_id=room_id,
            total_days=5)         
        
        delete_response = self.delete_booking(booking.data.get('id'), access_2)
        msg_wanted = delete_response.data.get('detail')

        get_response = self.get_booking_object(booking.data.get('id'), access=access_2)

        self.assertEqual(get_response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(delete_response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(str(msg_wanted), 'Você não tem permissão para executar essa ação.')


    def test_user_can_get_other_booking(self):
        ...
        

        


