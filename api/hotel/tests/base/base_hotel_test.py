from django.urls import reverse
from rest_framework import test
from .hotel_mixins import HotelMixin


class HotelTestBase(test.APITestCase, HotelMixin):
    def setUp(self) -> None:
        
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()