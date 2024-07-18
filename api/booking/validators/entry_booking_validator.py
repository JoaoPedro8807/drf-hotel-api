from collections import defaultdict
from rest_framework.validators import ValidationError
from django.conf import settings
from datetime import datetime, timedelta


class BookingEntryValidator:
    """
    A class to validate the entry data  and extra roles from booking endpoint 
    """

    def __init__(self, data):
        self.errors = defaultdict(list)
        self.data = data
        self.clean()

    def clean(self):
        self.clean_days()
        self.clean_booking_date()

        if self.errors: 
            raise ValidationError(self.errors)

    def clean_days(self):
        days = self.data.get('days')
        MIN_DAYS = int(settings.BOOKING_MIN_DAYS)
        if not days in range(1, MIN_DAYS):
            self.errors['days'].append(f'The number of days must be between 1-{MIN_DAYS}')
        return days
    
    def clean_booking_date(self):
        total_days = int(self.data.get('days')) #this field is required
        try: 
            start_date = self.data['start_date'] #these fields is not required
            end_date = self.data['end_date']
            
        except KeyError:
            start_date = datetime.now().date()
            end_date = start_date  + timedelta(days=total_days)


        if start_date != datetime.now().date():
            self.errors['start_date'].append(f'The date {start_date} is incorrect, try again')
        
        expected_end =  (datetime.strptime(str(start_date), '%Y-%m-%d') + timedelta(days=total_days)).date()
        if expected_end != end_date:
            print('expected: ', expected_end, 'end_date: ', end_date)
            self.errors['start_date'].append('the date received dont meet to end date')


    
        