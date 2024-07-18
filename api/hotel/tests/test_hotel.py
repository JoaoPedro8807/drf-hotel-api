from django.urls import reverse
from rest_framework import status
from parameterized import parameterized
from .base.base_hotel_test import HotelTestBase
from hotel.models.hotel_model import Hotel
from rest_framework.exceptions import ErrorDetail
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
        print('create_response', create_response.status_code, create_response.data)
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(str(create_response.data.get('hotelier')), hotelier_user) 
        
    
   


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
        guest_id = create_guest.data.get('user_info').get('guest_id')
        ...
        login_guest = self.client.post(
            self.urls.get('login'),
            data=data
        )
        create_response = self.make_hotel(
            hotelier_user=guest_id,
            access_token=login_guest.data.get('access')
        )
        self.assertRaisesMessage(expected_exception=ErrorDetail, expected_message=f'Pk inválido "{guest_id}" - objeto não existe.')
        self.assertEqual(create_response.status_code, status.HTTP_400_BAD_REQUEST)
        
        
    def test_hotelier_can_edit_your_hotel(self):
        hotel = self.make_login_and_hotel()
        hotel_id = str(hotel['create_response'].data.get('hotel_id'))
        access_token = hotel['login_response'].data.get('access')
        hotelier = hotel.get('create_response').data.get('hotelier')
        patch_data = {
            "hotelier": str(hotelier),
            "name": "Testando hotel",
            "stars_class": 5,
        }            
        url = reverse('hotel:hotel_viewset-detail', args=[hotel_id])
        response = self.client.patch(
            url,
            data=json.dumps(patch_data),
            content_type='Application/json',
            HTTP_AUTHORIZATION=f'Bearer {access_token}'
        )
        print('ALTERACAO: ', response.data, 'CODE: ', response.status_code)

        expected_name = patch_data.get('name')
        expected_stars_class = patch_data.get('stars_class')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), expected_name)
        self.assertEqual(response.data.get('stars_class'), expected_stars_class)
        

    def test_hotel_name_unique_constraint_(self):
        hotel1 = self.make_login_and_hotel() #with default values

        hotel2_hotelier = self.make_login_hotelier(email='TestandoHotel2@gmail.com', extra_fields={'document': '1231231231'}) #skip from the others uniques constraints
        hotelier_id = hotel2_hotelier.data.get('user_info').get('hotelier_id')
        hotel2_hotel = self.make_hotel(
            hotelier_user=hotelier_id,
            access_token=hotel2_hotelier.data.get('access')
        )   
        
        print('DATAA: ', hotel2_hotel.data)
        self.assertEqual(hotel2_hotel.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaisesMessage(expected_exception=ErrorDetail, expected_message="{'name': [ErrorDetail(string='hotel com este name já existe.', code='unique')]}")


    def test_hotelier_can_create_just_one_hotel(self):
        reponses = self.make_login_and_hotel() #hotel1
        hotelier_response = reponses.get('login_response')
        hotelier_id = hotelier_response.data.get('user_info').get('hotelier_id')

        hotel2_response = self.make_hotel(
            hotelier_user=hotelier_id,
            access_token=hotelier_response.data.get('access'),
            extra_data={
                'name': 'TestandoSegundoHotel'
            }
        ) 
        self.assertRaisesMessage(expected_exception=ErrorDetail, expected_message="{'hotelier': [ErrorDetail(string='hotel com este hotelier já existe.', code='unique')]}")
        self.assertEqual(hotel2_response.status_code, status.HTTP_400_BAD_REQUEST)


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
        
