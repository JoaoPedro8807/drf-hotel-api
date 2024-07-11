from django.urls import reverse

class BookingEditMixin:
    def delete_booking(self, booking_id: str, access: str):
        return self.client.delete(
            reverse('booking:booking_viewset-detail', args=[booking_id]),
            HTTP_AUTHORIZATION = f'Bearer {access}'
        )
    def get_booking_object(self, booking_id: str, access: str):
        return self.client.get(
            reverse('booking:booking_viewset-detail', args=[booking_id]),
            HTTP_AUTHORIZATION = f'Bearer {access}'
        )