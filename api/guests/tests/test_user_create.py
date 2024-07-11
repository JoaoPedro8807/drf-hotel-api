from .base import UserAuthModelBaseTest
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.validators import ValidationError as DRFValidationError
from django.core.exceptions import ValidationError as DjangoValidationError
from parameterized import parameterized


class UserCreateTest(UserAuthModelBaseTest):
    """
        Only UserAuth model  tests, create user and login user are separated 
    """
    def test_e(self):
        self.assertEqual(1, 1)

    def test_user_auth_model(self):
        user = self.user_model
        self.assertIsInstance(user, get_user_model())
        

    def test_user_auth_model_only_accepts_type_user(self):
        with self.assertRaises(DjangoValidationError):
            user = self.make_user_model(type_user='qualquercoisa')


    def test_email_unique_contraint_user(self):
        with self.assertRaises(DjangoValidationError, msg='Usuário com este User email já existe.'):
            user1 = self.make_user_model(username='user1') #now, email is the only required and unique field, on the UserAuth model
            user2 = self.make_user_model(username='user2')

    @parameterized.expand([
        ('email', 50),
        ('username', 50),
        ('type_user', 2)
    ])
    def test_user_auth_fields_max_length(self, field, max_length):
        setattr(self.user_model, field, 'A' * (max_length + 1))
        with self.assertRaises(DjangoValidationError):
            self.user_model.full_clean()

    def test_user_staff_status_is_correct(self):
        user = self.make_user_model(email='user1teste@gmail.com', is_staff=True)
        self.assertTrue(user.staff)
        
    def test_user_password_invalid_requirements(self):
        with self.assertRaises(DjangoValidationError):
            user = self.make_user_model(email='teste123@gmail.com', password='123')
        
