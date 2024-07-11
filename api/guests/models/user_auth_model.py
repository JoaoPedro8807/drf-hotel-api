from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework.validators import ValidationError
from django.core.exceptions import ValidationError as DjangoValidationError
import re
from .abstract_model import BaseAbstractModel
from .managers.user_auth_manager import UserManager
import os
import json


type_user_env = os.environ.get('HOTEL_USERS_TYPES', None)
TYPES_USERS = (
    ('GS', 'Guest'),
    ('HL', 'Hotelier' )
    )


print('TYPE_USERS: ', TYPES_USERS)


class UserAuth(AbstractBaseUser, PermissionsMixin, BaseAbstractModel): #Model primário tanto para guets e hotelier
   
    objects = UserManager()
    email = models.EmailField(_("user email"), max_length=50, unique=True)
    username = models.CharField(_("user name"), max_length=50, blank=False, null=False)
    is_staff = models.BooleanField(_("staff user field"), default=False)
    is_active = models.BooleanField(_("active bool field"), default=True)
    is_superuser = models.BooleanField(_("super user field"), default=False)
    type_user = models.CharField(_("type of user, hotelier or guest"), max_length=2, choices=TYPES_USERS, null=False, blank=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'type_user'] #fields to create user and superuser

    def __str__(self) -> str:
        return f'{self.username} - ({self.email})'     
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = 'user_auth'

    @property
    def staff(self):    
        return self.is_staff
    
    @property
    def especific_user(self):
        if hasattr(self, 'guest_user'):
            return self.guest_user
        
        elif hasattr(self, 'hotelier_user'):
            return self.hotelier_user
        
        return None
    
    #clean methods
    def clean(self) -> None:    
        self.clean_password() #our clean_password, AbstractUser has other
        return super().clean()

    def clean_password(self):
        reg_string = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,30}$' #a lower and upper word, a number and 8-30 chars
        password = self.password
        if not re.match(reg_string, password):
            raise DjangoValidationError('A senha não atende aos requisitos')

        return password
    
    def clean_type_user(self):
        self.type_user.upper()
        type_user_field = self.type_user
        if not type_user_field in TYPES_USERS.keys():
            raise DjangoValidationError('Tipo de usuário inválido, por favor, selecione um válido.')

        if not type_user_field:
            raise DjangoValidationError('Não foi passado nenhum tipo de usuário, por favor, selecione um.')

        return type_user_field      

   
    def clean_username(self):
        reg_string = r'^[a-zA-Z]{1,20}$'
        username = self.username
        if not re.match(reg_string, username):
            raise DjangoValidationError('Username não corresponde aos requisitos, tente novamente')
        
        return username
    
        





