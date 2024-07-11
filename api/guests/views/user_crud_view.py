from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from rest_framework import status
from ..serializers import UserAuthSerializer
from ..permissions import Owner
from ..serializers import GuestUserSerializer
from hotelier.serializers.hotelier_serializer import HotelierSerializer
from ..services.filter_especific_fields_user import filter_especific_fields
from rest_framework.exceptions import ValidationError as DRFValidationError
from django.db import IntegrityError, transaction
from ..services import create_guest, create_hotelier_user
from django.core.exceptions import ValidationError


UserAuthModel = get_user_model()

class UserCrudViewSet(viewsets.ModelViewSet):  
    User = get_user_model()
    queryset = User.objects.all()
    http_method_names = ['post', 'patch', 'delete']   
    serializer_class = UserAuthSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny(),]
        return [Owner(), ]

    def get_object(self):
        id = self.kwargs.get('id', '') 
        User = get_user_model()
        try:
            obj = get_object_or_404(
                self.get_queryset(),
                uuid=id
            )
            self.check_object_permissions(request=self.request, obj=obj)
            return obj
        
        except (KeyError, ValueError, User.DoesNotExist) as e:
            return Response({'error': f'Usuário não encontrado, {str(e)}'})

    def create(self, request, *args, **kwargs):
        user_auth_serializer = UserAuthSerializer(
            data=request.data,
            context = {'request': request}
            )
        user_auth_serializer.is_valid(raise_exception=True)
        validated_user_data = user_auth_serializer.validated_data

        type_user = request.data.get('type_user')
        type_user_serializer = {
                'HL': HotelierSerializer, 
                'GS': GuestUserSerializer
            }         
        especific_serializer = type_user_serializer.get(type_user)
        extra_fields = filter_especific_fields(request.data, especific_serializer)
        teste = especific_serializer(data=extra_fields, context={'request': request})
        teste.is_valid(raise_exception=True)

     

        with transaction.atomic():
            try:
                auth_user = UserAuthModel.objects.create_user(
                    **validated_user_data,
                )
                if type_user == 'GS':
                    create_guest(auth_user=auth_user, fields=extra_fields)
                else: #validate_data test model_choices for type_user before, so this is safe
                    create_hotelier_user(auth_user=auth_user, fields=extra_fields)

                repesentation = UserAuthSerializer().to_representation(instance=auth_user)
                return Response(repesentation, status=status.HTTP_201_CREATED)

            except (ValidationError, IntegrityError) as error:
                raise DRFValidationError(error.error_dict)
    
            except Exception as e:
                raise DRFValidationError({'detail': str(e)})
                      
    @action(
        methods=['PATCH'],
        detail=True
        )
    def change(self, request, *args, **kwargs):
        user = self.get_object()
        type_user_serializer = {
                'HL': HotelierSerializer(), 
                'GS': GuestUserSerializer()
            }      
        try:
            especific_user_serializer = type_user_serializer.get(user.type_user)
            extra_fields = filter_especific_fields(request.data, especific_user_serializer)
            especific_user_instance = user.especific_user #att the user_especific in your serializer
            
            user_update = especific_user_serializer.update(
                especific_user_instance, 
                extra_fields)   
            user_update.save()
            
            serializer = self.get_serializer(
                instance=user,
                data=request.data,
                many=False,
                context={'request': request},
                partial=True,
            )   
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer=serializer) #from super().update 
            serializer.save()
            return Response(serializer.data)
        
        except Exception as e:
            print('ERRO AO PEGAR O USER OBJECT', e)
            return Response(
                {'detail': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST)

    @action(
    methods=['DELETE',],
    detail=True
    )
    def remove(self, request, *args, **kwargs):
        try:
            user = self.get_object()
            user.delete()
            return Response({'detail': f'Usuário deletado com sucesso!'}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
            {'detail': str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )
  

            