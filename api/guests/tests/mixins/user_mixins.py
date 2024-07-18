from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class UserAtuhModelMixin:
    def make_user_model(
            self,
            type_user: str = 'GS',
            email:str = 'criandoteste@gmail.com',
            password:str = 'Testepassword123',
            username:str = 'username_teste',
            is_staff:bool = False,
            is_active: bool = True,
            is_superuser:bool = False,                                                                      
            ):
        return User.objects.create_user(
            type_user=type_user,
            email=email,
            password=password,
            username=username,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser
        )
    

class UserAPIMixin(UserAtuhModelMixin):
    def     make_user_data(
            self,
            email:str = 'criandoteste@gmail.com',
            password:str = 'Testepassword123',
            username:str = 'username_teste',            
            phone_number:str = '1234321312',
            type_user:str = 'GS' ,
            document:str = '213122312312',
            first_name:str = 'first_name_teste',
            last_name:str = 'last_name_teste',
            ):
        data = {
            'email': email,
            'password': password,
            'username': username,
            'phone_number': phone_number,
            'type_user': type_user,
            'document': document,
            'first_name': first_name,
            'last_name': last_name
        }
        return data        

    def get_user_logged(self, email: str ='testandologin@gmail.com', password: str ='TestandoLogin123!', extra_data=None) -> dict:
        user_data = {
            'email': email,
            'password': password,
            **extra_data
        }
        user = self.make_user_model(**user_data)
        url_login = reverse('guests:login')
        response = self.client.post(
            url_login, 
            data={'email': user_data.get('email'), 'password': user_data.get('password')})
        
        return {
            'access_token': response.data.get('access'),
            'refresh_token': response.data.get('refresh'),
            'user_id': response.data.get('user_id'),
            'user': user,
        }
        
    def make_user_api(self, data):
        return self.client.post(
            reverse('guests:user_create'),
            data={**data}
         )
    
    def make_login_user(self, data):
        url_login = reverse('guests:login')
        response = self.client.post(
            url_login, 
            data={**data})
        
        return response        
