from django.urls import reverse
from rest_framework import test
from . import RoomMixin


class RoomTestBase(test.APITestCase, RoomMixin):
    def setUp(self) -> None:
        
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()