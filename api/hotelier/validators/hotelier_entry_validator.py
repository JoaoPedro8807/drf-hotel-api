from collections import defaultdict
from rest_framework.validators import ValidationError
import re
class HotelEntryValidator:
    def __init__(self, data):
        self.errors = defaultdict(list)
        self.data = data
        self.clean()

    def clean(self):
        self.clean_document()
        self.clean_first_name()
        self.clean_phone_number(0)
        
        if self.errors:
            ValidationError(self.errors)

    def clean_document(self):
        cnpj = self.data.get('document')
        reg_string = '^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$'
        if not re.match(reg_string, cnpj):
            self.errors['document'].append(f'CNPJ {cnpj} is incorrect, send a correct cnpj!')
        
    def clean_first_name(self):
        value = self.data.get('first_name')
        reg_string = r'^[a-zA-Z0-9._]{3,20}$'
        if not re.match(reg_string, value):
            self.erros['first_name'].append('The first name must be match requirements')
        return value

    def clean_phone_number(self):
        pn = self.data.get('phone_number')
        reg_string = r'^\(?\d{2}\)?[\s-]?\d{4,5}[-]?\d{4}$'
        if not re.match(reg_string, pn):
            self.erros['phone_number'].append(f'Phone number {pn} invalid!')
                        
