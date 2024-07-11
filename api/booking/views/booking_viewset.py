from rest_framework import viewsets, mixins
from ..models.booking_model import Booking
from rest_framework.permissions import IsAuthenticated
from ..serializers.booking_serizlier import BookingSerializer
from ..permissions import BookingPermission
from ..services import att_available_room
from rest_framework.validators import ValidationError as APIValidationError
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import status
from django.core.mail import send_mail



class BookingViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    """
    viewset to create, delete, retrive a booking    
    """
    queryset = Booking.objects.all()
    http_method_names  = ['post', 'delete', 'get']
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, BookingPermission]



    def get_object(self):
        return super().get_object()
