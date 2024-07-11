import json
from django.urls import reverse
from guests.tests.base.user_test_base import UserAPIMixin
from ...models import Hotel
class HotelMixin(UserAPIMixin):
    urls = {
    'create_user': reverse('guests:user_create'),
    'login': reverse('guests:login')
    }
    
    def make_login_hotelier(self, email: str = 'testando@gmail.com', password:str = 'Testandooo123!', extra_fields={}):
        data = {
            'type_user': "HL",
            'email': email,
            'password': password,
            **extra_fields
        }
        hotelier_data = self.make_user_data(**data)
        user = self.client.post(
            self.urls.get('create_user'),
            data={**hotelier_data}
        )
        login = self.client.post(
            self.urls.get('login'),
            data={
                'email': data.get('email'),
                'password': data.get('password')
            })
        return login            
    
    
    
    def make_hotel_data(
            self,
            hotelier:str = None,
            name:str = 'Testando',
            total_rooms: int = 10,
            stars_classs: int = 3,
            rooms:list[object] =  [
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
                },
                {
                    "room_number": 3,
                    "room_type": "D",
                    "daily_price": "200.00",
                    "available": True
                },
                {
                    "room_number": 4,
                    "room_type": "S",
                    "daily_price": "150.00",
                    "available": True
                },
                {
                    "room_number": 5,
                    "room_type": "D",
                    "daily_price": "200.00",
                    "available": True
                },
                {
                    "room_number": 6,
                    "room_type": "S",
                    "daily_price": "150.00",
                    "available": True
                },
                {
                    "room_number": 7,
                    "room_type": "S",
                    "daily_price": "150.00",
                    "available": True
                },
                {
                    "room_number": 8,
                    "room_type": "S",
                    "daily_price": "150.00",
                    "available": True
                },
                {
                    "room_number": 9,
                    "room_type": "S",
                    "daily_price": "150.00",
                    "available": True
                },
                {
                    "room_number": 10,
                    "room_type": "S",
                    "daily_price": "150.00",
                    "available": True
                }
            ]):
        return {
            "hotelier": hotelier,
            "name": name,
            "total_rooms": len(rooms),
            "stars_class": stars_classs,
            "rooms": rooms
        }
    def make_hotel_object(self, hotelier):
        data = self.make_hotel_data(hotelier=hotelier)
        Hotel.objects.create(**data)
    
    
    def make_hotel(self, hotelier_user, access_token, extra_data={}):
        hotel_data = self.make_hotel_data(hotelier=hotelier_user, **extra_data)
    
        response = self.client.post(
            reverse('hotel:hotel_viewset-list'),
            data=json.dumps(hotel_data),
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer {access_token}'
            )
        return response
        

    def make_login_and_hotel(self):
        hotelier_auth = self.make_login_hotelier()
        hotelier_user = hotelier_auth.data.get('user_info').get('hotelier_id')
        access_token = hotelier_auth.data.get('access')

        create_response = self.make_hotel(
            hotelier_user=hotelier_user,
            access_token=access_token
        )
        response = {
            'create_response': create_response,
            'login_response': hotelier_auth
        }
        return response
        
        




            
