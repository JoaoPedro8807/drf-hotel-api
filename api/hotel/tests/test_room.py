from django.urls import reverse
from rest_framework import status
from parameterized import parameterized
from .base.base_room_test import RoomTestBase
from hotel.models.hotel_model import Hotel
from rest_framework.exceptions import ErrorDetail
import json

class HotelTest(RoomTestBase):
    def test_room(self):
        response = self.make_room_and_hotel()
        print('RESPONSE: ', response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_hotel_has_correct_number_of_rooms(self):
        hotelier_auth = self.make_login_hotelier()
        hotelier_user = hotelier_auth.data.get('user_info').get('hotelier_id')
        access_token = hotelier_auth.data.get('access')

        
        create_response = self.make_hotel(
            hotelier_user=hotelier_user,
            access_token=access_token,
        )
        print('DATA DESSE CARALHO: ', create_response.data)

        rooms_from_api = create_response.data.get('rooms')
        rooms_return = [
            {
                "room_number": room.get("room_number"),
                "room_type": room.get("room_type"),
                "daily_price": room.get("daily_price"),
                "available": room.get("available")
            }
                for room in rooms_from_api
            ]   #without uuid and details (we havent without model)
        
        
        #t = list(map(lambda room: room.pop('id', 'detail'), rooms_from_api)) #here, we havent the uuid from model


        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)        

