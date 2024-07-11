from django.urls import reverse
from guests.tests.base.user_test_base import UserAPIMixin

class HotelierMixin(UserAPIMixin):
    def get_hotelier_urls(self):
        ...


    def make_hotelier_data(
            document: str = '123123123',
            phone_number: str = '1231231313',
            first_name:str = 'testando hotelier',
            last_name:str = 'hotelier',
            ):
        return {
            "document": document,
            "phone_number": phone_number,
            "first_name": first_name,
            "last_name": last_name
        }
    

    def make_hotelier_user(self):
        response = self.client.post(
            reverse()
        )
        

