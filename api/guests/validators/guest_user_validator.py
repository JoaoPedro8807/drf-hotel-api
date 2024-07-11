from collections import defaultdict
import re
from rest_framework.validators import ValidationError
class UserGuestValidator:
    def __init__(self, data, erros=None) -> None:
        self.erros = defaultdict(list)
        self.data = data
        self.clean()
        

    def clean(self):    
        self.clean_first_name()
        if self.erros:
            raise ValidationError(self.erros)


    def clean_first_name(self):
        value = self.data.get('first_name')
        reg_string = r'^[a-zA-Z0-9._]{3,20}$'
        if not re.match(reg_string, value):
            self.erros['first_name'].append('The first name must be match requirements')
        return value
       

        