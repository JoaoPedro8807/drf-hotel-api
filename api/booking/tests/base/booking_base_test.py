from rest_framework import test
from .booking_test_mixin import BookingTestMixin
from django.urls import reverse

class BookingTestBase(test.APITestCase, BookingTestMixin):
    ...         