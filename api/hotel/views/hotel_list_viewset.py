from rest_framework import viewsets
from ..models import Hotel
from ..serializers.hotel_list_serializer import HoteListSerializer, HotelDetailSerializer 
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.utils.cache import get_cache_key
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings

class ListHotelPagination(PageNumberPagination):
    page_size = 10  

class ListHotelViewset(viewsets.GenericViewSet, viewsets.mixins.ListModelMixin):
    """
    a viewset to show all hotels, and your respective link to detail 
    """

    CACHE_PREFIX = 'hotel-model-list'

    queryset = Hotel.objects.prefetch_related('rooms').all()  
    permission_classes = [AllowAny]
    pagination_class = ListHotelPagination
    serializer_class = HoteListSerializer   

    @method_decorator(cache_page((int(settings.TIME_CACHE_LIST_VIEWS) * 60), key_prefix=CACHE_PREFIX)) 
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    

class HotelDetailViewSet(viewsets.GenericViewSet, viewsets.mixins.RetrieveModelMixin):
    CACHE_PREFIX = 'hotel-model-list'
    """
    a view only accept retrive to show detail, here use HotelDetailSerializer (have more information)
    """
    queryset = Hotel.objects.prefetch_related('rooms').all()  
    permission_classes = [IsAuthenticated]
    serializer_class = HotelDetailSerializer
    lookup_field = 'id'
    lookup_value_regex = r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"

    @method_decorator(cache_page((int(settings.TIME_CACHE_LIST_VIEWS) * 60), key_prefix=CACHE_PREFIX)) 
    def retrieve(self, request, *args, **kwargs): #get object with all details
        return super().retrieve(request, *args, **kwargs)