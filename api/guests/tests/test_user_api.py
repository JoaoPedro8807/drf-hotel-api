from .base import UserAPIBaseTest
from django.urls import reverse
from rest_framework import status
from parameterized import parameterized
from django.core.exceptions import ValidationError


class UserAPITest(UserAPIBaseTest):
    def test_user_login(self):
        user_data = {
            'email': 'Testlogin@gmail.com',
            'password': 'testeLogin123!'
        }
        user = self.make_user_model(**user_data)
        url_login = reverse('guests:login')
        response = self.client.post(url_login, data={**user_data})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest_user_api(self):
        user_data = self.make_user_data()
        response = self.make_user_api(data=user_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_hotelier_user(self):
        user_data = self.make_user_data(type_user='HL')
        print('USERDATA: ', user_data)
        response = self.make_user_api(data=user_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_user_can_update_your_instance(self): #testar erro de mudar outra instancia tmb
        test_data = {
            'email': 'Testlogin@gmail.com',
            'password': 'testeLogin123!'
        }
        user_data = self.make_user_data(
            email=test_data.get('email'), 
            password=test_data.get('password'))        
        
        response_create = self.make_user_api(data=user_data)
        user_id = response_create.data.get('user_id')
        
        login_response = self.make_login_user(data={**test_data})   
        jwt_access_token = login_response.data.get('access')

        first_name_wanted = 'alterando o first_name'

        response = self.client.patch(   
            reverse('guests:user_edit', args=[user_id]),
            data={'first_name': first_name_wanted},
            headers={'Authorization': f'Bearer {jwt_access_token}'}
        )
        ...
        new_first_name = response.data.get('user_info').get('first_name')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_first_name, first_name_wanted)

    def test_user_cant_update_other_user(self):
        user1_data = {
            'email': 'user1teste@gmail.com',
            'password': 'Testando123321!'
        }
        user1 = self.make_user_api(
            self.make_user_data(email=user1_data.get('email'), password=user1_data.get('password')))
        
        user2 = self.make_user_api(
            self.make_user_data(
                email='user2teste@gmail.com',
                document='21312231312'))
        user2_id = user2.data.get('user_id')
        
        login_response = self.make_login_user({'email': user1_data.get('email'), 'password': user1_data.get('password')})
        jwt = login_response.data.get('access')

        response = self.client.patch(
            reverse('guests:user_edit', args=[user2_id]),
            data={'first_name': 'não era pra ser alterado'},
            headers={'Authorization': f'Bearer {jwt}'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data.get('detail'), 'Você não tem permissão para executar essa ação.')

        
    def test_unique_constraint_user_document(self):
        user1_response = self.make_user_api(
            self.make_user_data(email='user1testando@gmail.com'))
        
        user2_response = self.make_user_api(
            self.make_user_data(email='user2teste@gmail.com'))# now, document is the only field required
        ...
        self.assertEqual(user2_response.status_code, status.HTTP_400_BAD_REQUEST)        
        
    def test_user_can_delete_yourself(self):
        user_data = {
            'email': 'user1teste@gmail.com',
            'password': 'Testando123321!'
        }
        user = self.make_user_api(
            self.make_user_data(email=user_data.get('email'), password=user_data.get('password')))
        user_id = user.data.get('user_id')

        login = self.make_login_user({'email': user_data.get('email'), 'password': user_data.get('password')})
        jwt = login.data.get('access')
        
        response = self.client.delete(
            reverse('guests:user_edit', args=[user_id]),
            headers={'Authorization': f'Bearer {jwt}'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)   


    def test_user_cant_delete_other_user(self):
        user1_data = {
            'email': 'user1teste@gmail.com',
            'password': 'Testando123321!'
        }
        user1 = self.make_user_api(
            self.make_user_data(email=user1_data.get('email'), password=user1_data.get('password')))
        
        user2 = self.make_user_api(
            self.make_user_data(
                email='user2teste@gmail.com',
                document='21312231312'))
        user2_id = user2.data.get('user_id')
        
        login_response = self.make_login_user({'email': user1_data.get('email'), 'password': user1_data.get('password')})
        jwt = login_response.data.get('access')

        response = self.client.delete(
            reverse('guests:user_edit', args=[user2_id]),
            data={'first_name': 'não era pra ser alterado'},
            headers={'Authorization': f'Bearer {jwt}'}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('detail'), 'Você não tem permissão para executar essa ação.')        

    def test_user_first_name_dont_match_requirements(self):
        first_name = 'a' * 31
        user_data = self.make_user_data(first_name=first_name)        
        user_response = self.make_user_api(
            data=user_data
        )
        msg = user_response.data.get('first_name')[0]
        self.assertEqual(user_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(msg), 'The first name must be match requirements')
        

    def test_user_password_dont_match_requirements(self):
        password = 'a' * 31
        user_data = self.make_user_data(password=password)        
        user_response = self.make_user_api(
            data=user_data
        )
        msg = user_response.data.get('password')[0]
        self.assertEqual(user_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(msg), 'The password must have at least: 1 uppercase and lowercase letter, 1 number and 8 to 30 characters')

    def test_user_with_incorrect_type_user(self):
        type_user = 'a' 
        user_data = self.make_user_data(type_user=type_user)        
        user_response = self.make_user_api(
            data=user_data
        )
        msg = user_response.data.get('type_user')[0]
        self.assertEqual(user_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(msg),  '"a" não é um escolha válido.')
                




        
#headers={'Authorization': f'Bearer {user_auth.get('access_token')}'}

