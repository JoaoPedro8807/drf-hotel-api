from django.test import TestCase
from ..base.booking_test_mixin import BookingTestMixin

class CeleryTestBase(TestCase, BookingTestMixin):
    def setUp(self) -> None:
        # self.user_data = self.make_user_data()
        # guest_response = self.make_user_api(data=self.user_data).data
        # self.user_guest = str(guest_response.get('user_info').get('guest_id'))
        # self.user_guest_login = self.make_login_user(
        #     data={'email': self.user_data.get('email'), 
        #           'password': self.user_data.get('password')})

        # self.room = self.make_room_and_hotel().data
        # #self.room = Room.objects.create(hotel=self.hotel)
        # self.booking = self.make_only_booking(
        #     guest_id=self.user_guest,
        #     access=self.user_guest_login.data.get('access'),
        #     room_id=self.room.get('id'),
        #     total_days=5
        # ).data
        return super().setUp()
        
        