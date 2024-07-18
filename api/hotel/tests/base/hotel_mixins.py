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
            stars_classs: int = 3,      
            hotel_description: str = 'tararararadadawrara',
            rating: float = 9.9,
            street: str = 'Rua tarara',
            city: str = 'city tarara',
            state:str = 'state tararara',
            zip_code: str = '123321'
            ):
        return {
            "hotelier": hotelier,
            "name": name,
            "stars_class": stars_classs,
            "hotel_description": hotel_description,
            "rating": rating,
            "street": street,
            "city": city,
            "state": state,
            "zip_code": zip_code

        }
    def make_hotel_object(self, hotelier):
        data = self.make_hotel_data(hotelier=hotelier)
        Hotel.objects.create(**data)
    
    
    def make_hotel(self, hotelier_user, access_token, extra_data={}):
        hotel_data = self.make_hotel_data(hotelier=hotelier_user, **extra_data)
        print('DATA INDO PRO REQUEST', json.dumps(hotel_data))
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
        
        
    



            
