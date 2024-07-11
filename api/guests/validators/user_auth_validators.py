from collections import defaultdict
from rest_framework.serializers import ValidationError
import re
from django.contrib.auth import get_user_model
import os
import json
from django.conf import settings
class UserAuthValidator: 
    """
    class mais genérica para ambas ações em guest, limpa todos os fields e levanta erros (inclusive antecedentes) com a classe passada
    """
    def __init__(self, data, ErrorClass=ValidationError):
        self.errors = defaultdict(list) 
        self.ErrorClass = ErrorClass 
        self.data = data
        self.clean()

    def clean(self, *args, **kwargs):
        print('INICIANDO O CLEAN COM DATA: ', self.data)
        self.clean_password()
        self.clean_type_user()
        self.clean_username()

        if self.errors:
            print('levantando esses erros: ', self.errors)
            raise ValidationError(self.errors)
        

        
    def clean_username(self):
        reg_string = r'^[a-zA-Z0-9._]{3,20}$'
        username = self.data.get('username', '')
        if not re.match(reg_string, username):
            self.errors['username'].append('O nome precisa atender aos requisitos')
        return username   

    def clean_password(self):
        reg_string = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,30}$' #a lower and upper word, a number and 8-30 chars
        password = self.data.get('password')
        if not re.match(reg_string, password):
            self.errors['password'].append('The password must have at least: 1 uppercase and lowercase letter, 1 number and 8 to 30 characters')
        return password

    def clean_type_user(self):
        type_user_field = self.data.get('type_user', '')
        TYPES_USER = settings.HOTEL_USERS_TYPES
        if not type_user_field.upper() in TYPES_USER:
            self.errors['type_user'].append('Type of user is invalid. Please, select a valid choice')

        if not type_user_field:
            self.errors['type_user'].append('Não foi passado nenhum tipo de usuário, por favor, selecione um.')

        return type_user_field      

    def clean_phone_number(self):
        phone_number = self.data.get('phone_number')
        if len(phone_number) < 10:
            self.errors['phone_number'].append('Número de telefone inválido')
            
        return phone_number


    