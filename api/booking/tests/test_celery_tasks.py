from django.test import TestCase
from booking.tasks import send_email_booking_confirmation_task, booking_att_task, post_booking
from unittest.mock import patch
from .base import CeleryTestBase
from datetime import datetime, timedelta

class CeleryTasksTest(CeleryTestBase):
    @patch('booking.tasks.send_email_booking_confirmation_task.delay')
    def test_send_email_booking_confirmation(self, mock_send_email):
        all_booking_data = self.make_all_booking_data(all_data=True)

        guest_data = all_booking_data.get('guest_data')
        booking_response = all_booking_data.get('booking_response').data

        decimal_price = float(booking_response.get('price'))

        mock_send_email.assert_called_once()
        mock_send_email.assert_called_once_with(
            email=guest_data.get('email'),
            user_name=guest_data.get('username'),
            room_detail=booking_response.get('room_detail'),
            price=decimal_price,
            end_date=booking_response.get('end_date')
        )

    @patch('booking.tasks.booking_att_task.apply_async')
    def test_booking_att_task(self, mock_att_available_room):
        DAYS = 5
        all_booking_data = self.make_all_booking_data(total_days=DAYS, all_data=True)
        booking_data = all_booking_data.get('booking_response').data
        
        end_date = (datetime.now() + timedelta(days=DAYS)).replace(second=0, microsecond=0)
        mock_att_available_room.assert_called_once()
        mock_att_available_room.assert_called_once_with(kwargs={'request_data': booking_data}, eta=end_date)