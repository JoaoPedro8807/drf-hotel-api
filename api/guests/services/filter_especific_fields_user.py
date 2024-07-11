from rest_framework.serializers import ModelSerializer
from rest_framework.validators import ValidationError

def filter_especific_fields(request_data: dict, serializer: ModelSerializer):
    especific_user_fields = {}
    try:
        for field in serializer.Meta.fields: #all fields in serializer.model
            if request_data.get(field): 
                especific_user_fields[field] = request_data.get(field)

        return especific_user_fields
            
    except (KeyError, ValueError) as error: 
        raise ValidationError({'detail' f'Erro ao pegar a chave do campo: {str(error)}'})

    except Exception as e:
        print('ERRO AO FILTRAR FIELDS: ', e)
        raise ValidationError({'detail': 'Erro ao filtrar os dados da requisição '})