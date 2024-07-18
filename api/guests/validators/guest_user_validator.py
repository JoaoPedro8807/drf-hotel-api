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
        self.clean_document()
        self.clean_phone_number()

        if self.erros:
            raise ValidationError(self.erros)


    def clean_first_name(self):
        value = self.data.get('first_name')
        reg_string = r'^[a-zA-Z0-9._]{3,20}$'
        if not re.match(reg_string, value):
            self.erros['first_name'].append('The first name must be match requirements')
        return value
       
    def clean_document(self):
        cpf = self.data.get('document')
        reg_string = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
        if not re.match(reg_string, str(cpf)):
            self.erros['document'].append(f'CPF {cpf} is invalid, try with a valid document')

    def clean_phone_number(self):
        pn = self.data.get('phone_number')
        reg_string = r'^\(?\d{2}\)?[\s-]?\d{4,5}[-]?\d{4}$'
        if not re.match(reg_string, pn):
            self.erros['phone_number'].append(f'Phone number {pn} invalid!')
        