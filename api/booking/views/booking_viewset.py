#type: ignore
from rest_framework import viewsets, mixins
from ..models.booking_model import Booking
from rest_framework.permissions import IsAuthenticated
from ..serializers.booking_serizlier import BookingSerializer
from ..permissions import BookingPermission
from rest_framework.validators import ValidationError as APIValidationError

class BookingViewSet(
        viewsets.GenericViewSet,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        mixins.DestroyModelMixin):
    """
    endpoint make and deleting  a booking, neddes logged as guest.
    this booking will att room and hotel status, send confirmation, send finalization email when booking is finish etc.
    """
    queryset = Booking.objects.all()
    http_method_names  = ['post', 'delete', 'get']
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, BookingPermission]

    def get_object(self):
        return super().get_object()
