from django.urls import reverse
from rest_framework import status
from parameterized import parameterized
from .base.base_hotel_test import HotelTestBase
from hotel.models.hotel_model import Hotel
import json
class HotelTest(HotelTestBase):
    def test_hotel(self):   
        self.assertEqual(1, 1)

    def test_hotelier_can_create_hotel(self):
        hotelier_auth = self.make_login_hotelier()
        hotelier_user = hotelier_auth.data.get('user_info').get('hotelier_id')
        access_token = hotelier_auth.data.get('access')

        create_response = self.make_hotel(
            hotelier_user=hotelier_user,
            access_token=access_token
        )
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(str(create_response.data.get('hotelier')), hotelier_user) 
        
    
    def test_hotel_has_correct_number_of_rooms(self):
        hotelier_auth = self.make_login_hotelier()
        hotelier_user = hotelier_auth.data.get('user_info').get('hotelier_id')
        access_token = hotelier_auth.data.get('access')

        rooms = {
            'rooms': [
                {
                "room_number": 1,
                "room_type": "S",
                "daily_price": "150.00",
                "available": True
            },
            {
                "room_number": 2,
                "room_type": "T",
                "daily_price": "250.00",
                "available": True
            }]
        }
        create_response = self.make_hotel(
            hotelier_user=hotelier_user,
            access_token=access_token,
            extra_data=rooms
        )
        expected_rooms = rooms.get('rooms')
        expected_total_rooms = len(expected_rooms)

        rooms_from_api = create_response.data.get('rooms')
        t = list(map(lambda room: room.pop('id'), rooms_from_api)) #here, we havent the uuid from model


        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(create_response.data.get('total_rooms'), expected_total_rooms)
        self.assertEqual(create_response.data.get('rooms'), expected_rooms)


    def test_guest_user_cant_create_hotel(self):
        data = {
            'email': 'testandoguest@gmai.com',
            'password': 'Testandoguest123!'
        }
        guest_data = self.make_user_data(**data)
        create_guest = self.client.post(
            self.urls.get('create_user'),
            data=guest_data
        )
        guest = create_guest.data.get('user_info').get('guest_id')
        ...
        login_guest = self.client.post(
            self.urls.get('login'),
            data=data
        )
        create_response = self.make_hotel(
            hotelier_user=guest,
            access_token=login_guest.data.get('access')
        )
        error_code = str(create_response.data.get('hotelier')[0])
        expected_error_message = f'Pk inválido "{guest}" - objeto não existe.'

        self.assertEqual(create_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error_code, expected_error_message)
        
        
    def test_hotelier_can_edit_your_hotel(self):
        hotel = self.make_login_and_hotel()
        hotel_id = str(hotel['create_response'].data.get('hotel_id'))
        access_token = hotel['login_response'].data.get('access')
        hotelier = hotel.get('create_response').data.get('hotelier')
        patch_data = {
            "hotelier": str(hotelier),
            "name": "Testando hotel",
            "stars_class": 5,
            "rooms": [
                {
                    "room_number": 1,
                    "room_type": "T",
                    "daily_price": "500.00",
                    "available": False
                }
            ]
        }            
        url = reverse('hotel:hotel_viewset-detail', args=[hotel_id])
        response = self.client.patch(
            url,
            data=json.dumps(patch_data),
            content_type='Application/json',
            HTTP_AUTHORIZATION=f'Bearer {access_token}'
        )
        original_room = patch_data.get('rooms')[0]
        expected_room = response.data.get('rooms')[0]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_room.get('room_type'), original_room.get('room_type'))
        self.assertEqual(expected_room.get('daily_price'), original_room.get('daily_price'))
        self.assertEqual(expected_room.get('available'), original_room.get('available'))
        

    def test_hotel_name_unique_constraint_(self):
        hotel1 = self.make_login_and_hotel() #with default values

        hotel2_hotelier = self.make_login_hotelier(email='TestandoHotel2@gmail.com', extra_fields={'document': '1231231231'}) #skip from the others uniques constraints
        hotelier_id = hotel2_hotelier.data.get('user_info').get('hotelier_id')
        hotel2_hotel = self.make_hotel(
            hotelier_user=hotelier_id,
            access_token=hotel2_hotelier.data.get('access')
        )   
        expected_message = 'hotel com este name já existe.'

        self.assertEqual(hotel2_hotel.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(hotel2_hotel.data.get('name')[0]),  expected_message)


    def test_hotelier_can_create_just_one_hotel(self):
        reponses = self.make_login_and_hotel() #hotel1

        hotelier_response = reponses.get('login_response')
        hotelier_id = hotelier_response.data.get('user_info').get('hotelier_id')

        hotel2 = self.make_hotel(
            hotelier_user=hotelier_id,
            access_token=hotelier_response.data.get('access'),
            extra_data={
                'name': 'TestandoSegundoHotel'
            }
        )           
        expected_msg = 'hotel com este hotelier já existe.'
        self.assertEqual(str(hotel2.data.get('hotelier')[0]), expected_msg)


    def test_hotelier_can_delete_your_hotel(self):
        responses = self.make_login_and_hotel()
        create_hotel = responses.get('create_response')
        hotel_id = str(create_hotel.data.get('hotel_id'))        

        login = responses.get('login_response')
        access_token = login.data.get('access')

        url = reverse('hotel:hotel_viewset-detail', args=[hotel_id])

        delete = self.client.delete(
            url,
            content_type='Application/json',
            HTTP_AUTHORIZATION=f'Bearer {access_token}'
        )
        query = Hotel.objects.all().exists()
        self.assertEqual(delete.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(query)


    def test_hotelier_cant_delete_other_hotel(self):
        hotel1 = self.make_login_and_hotel() 
        hotel1_create = hotel1.get('create_response')
        hotel1_id = hotel1_create.data.get('hotel_id')

        hotel2_hotelier = self.make_login_hotelier(email='TestandoHotel2@gmail.com', extra_fields={'document': '1231231231'}) #skip from uniques constraints
        hotel2_access_token = hotel2_hotelier.data.get('access') 
        hotelier_id = hotel2_hotelier.data.get('user_info').get('hotelier_id')
        hotel2_hotel = self.make_hotel(
            hotelier_user=hotelier_id,
            access_token=hotel2_access_token
        )   
        url = reverse('hotel:hotel_viewset-detail', args=[hotel1_id])
        response = self.client.delete(
            url,
            HTTP_AUTHORIZATION = f'Bearer {hotel2_access_token}'
        )
        expected_msg = 'Você não tem permissão para executar essa ação.'

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(str(response.data.get('detail')), expected_msg)
        
