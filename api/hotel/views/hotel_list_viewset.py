from rest_framework import viewsets
from ..models import Hotel
from ..serializers.hotel_list_serializer import HoteListSerializer, HotelDetailSerializer 
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class ListHotelPagination(PageNumberPagination):
    page_size = 10


class ListHotelViewset(viewsets.ReadOnlyModelViewSet):  
    queryset = Hotel.objects.all()  
    permission_classes = [AllowAny]
    pagination_class = ListHotelPagination
    serializer_class = HoteListSerializer
    lookup_field = 'id'
    lookup_value_regex = r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"

    
class HotelDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hotel.objects.all()  
    permission_classes = [AllowAny]
    serializer_class = HotelDetailSerializer
    lookup_field = 'id'
    lookup_value_regex = r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"
