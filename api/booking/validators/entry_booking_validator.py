from collections import defaultdict
from rest_framework.validators import ValidationError
from django.conf import settings

MIN_DAYS = int(settings.BOOKING_MIN_DAYS)

class BookingEntryValidator:
    """
    A class to validate the entry data  and extra roles from booking endpoint 
    """
    

    def __init__(self, data):
        self.errors = defaultdict(list)
        self.data = data
        self.clean()


    def clean(self):
        #call all clean_fields
        self.clean_days()

        if self.errors: 
            raise ValidationError(self.errors)

    
    def clean_days(self):
        days = self.data.get('days')
       
        if not days in range(1, MIN_DAYS):
            self.errors['days'].append(f'The number of days must be between 1-{MIN_DAYS}')
        return days

    
        