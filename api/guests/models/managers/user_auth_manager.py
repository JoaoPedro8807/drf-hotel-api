from django.contrib.auth.models import BaseUserManager
from django.db import transaction
from django.db import IntegrityError, OperationalError
from rest_framework.exceptions import ValidationError 
from django.core.exceptions import ValidationError as DjangoValidationError

class UserManager(BaseUserManager):
    """
    centralizes user creation for authentication and user specification in its own table.
    any exception the db_session rollback the transitions
    """
    def create_user(
            self, 
            email: str, 
            password: str, 
            username:str, 
            type_user: str, 
            is_superuser:bool = False, 
            is_staff:bool = False, 
            is_active:bool = True
            ):
        email = self.normalize_email(email) 
        with transaction.atomic():
            try:
                user = self.model(
                    email=email,                                                                                        
                    username=username,
                    password=password,
                    is_superuser=is_superuser,
                    is_staff=is_staff,
                    type_user=type_user,
                    is_active=is_active
                    )   
                user.full_clean()
                user.set_password(password)
                user.save(using=self._db)
                
            except (ValueError, IntegrityError) as e:
                raise DjangoValidationError({'detail': f'Dados inccoretos: {str(e)}'})
            
            except Exception as e:
                print('Erro ao criar UserAuth: ', e)                
                raise  DjangoValidationError({'detail': f'Erro ao criar usuário: {e}'})   

        return user
        

    def create_superuser(self, email:str, password:str, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Para criar super usuário, ele deve ser definido como is_staff primeiro ')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Para criar um superuser ele deve ser definido como issuperuser primeiro.')

        return self._create_user(email, password, **extra_fields)
    

    def get_especific_user(self):
        ...