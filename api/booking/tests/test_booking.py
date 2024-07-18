from .base.booking_base_test import BookingTestBase
from django.urls import reverse
import json
from rest_framework import status
from unittest.mock import patch
from hotel.models import Room
from ..models import Booking
from datetime import datetime, timedelta
from time import sleep
from django.conf import settings 
from rest_framework.validators import ValidationError


class BookingAPITest(BookingTestBase):
    def test_create_a_booking(self):
        room = self.make_room_and_hotel()
        room_id = str(room.data.get('id'))

        guest_data = self.make_user_data(
            email='testandobooking@gmail.com', 
            password = 'Testandobooking123!')
        guest_user = self.client.post(
            self.urls.get('create_user'),
            data={**guest_data}
        )        
        guest_login = self.client.post(
            reverse('guests:login'),
            data={
                'email': 'testandobooking@gmail.com',
                'password': 'Testandobooking123!'
            }
        )

        guest_id = guest_login.data.get('user_info').get('guest_id')
        access_token = guest_login.data.get('access')
  
        post_data = {
            'guest': str(guest_id),
            'room': room_id,
            'days': 5
        }   

        response = self.client.post(
            reverse('booking:booking_viewset-list'),
            content_type='Application/json',
            data=json.dumps(post_data),
            HTTP_AUTHORIZATION = f'Bearer {access_token}'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        

    def test_att_room_available_when_make_a_booking(self):
        booking = self.make_all_booking_data()
        room_id = booking.data.get('room')
        room = Room.objects.filter(
            id=str(room_id)
        ).first()
        self.assertFalse(room.available)



    def test_room_is_the_same_in_booking(self):
        guest_login, guest_auth = self.make_all_guest_data()
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
        self.assertEqual(room.data.get('room_number'), booking.data.get('room_detail').get('room_number'))

    @patch('booking.validators.entry_booking_validator.MIN_DAYS', new=3)
    def test_min_days_of_booking(self):
        response = self.make_all_booking_data(total_days=4)
        msg_wanted = response.data.get('days')[0]
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(msg_wanted), 'The number of days must be between 1-3')
        

    def test_price_of_booking_is_correct(self):
        guest_login, _ = self.make_all_guest_data()
        guest_id = guest_login.data.get('user_info').get('guest_id')
        access = guest_login.data.get('access')

        room = self.make_room_and_hotel()
        room_id = str(room.data.get('id'))

        room_price = room.data.get('daily_price')
        TOTAL_DAYS = 5
        real_price = round((float(room_price) * TOTAL_DAYS), 2)

        booking = self.make_only_booking(
            guest_id=guest_id,
            access=access,
            room_id=room_id,
            total_days=TOTAL_DAYS
        )        
        self.assertEqual(float(booking.data.get('price')), real_price)

    def test_end_date_is_correct(self):
        guest_login, _ = self.make_all_guest_data()
        guest_id = guest_login.data.get('user_info').get('guest_id')
        access = guest_login.data.get('access')

        room = self.make_room_and_hotel()
        room_id = str(room.data.get('id'))

        TOTAL_DAYS = 5
        booking = self.make_only_booking(
            guest_id=guest_id,
            access=access,
            room_id=room_id,
            total_days=TOTAL_DAYS
        )             
        wanted_end_date = str(datetime.now().date() + timedelta(days=TOTAL_DAYS)) 
        
        self.assertEqual(booking.data.get('end_date'), wanted_end_date)


        
