from rest_framework import viewsets
from rest_framework.views import APIView
from django.shortcuts import get_list_or_404
from ..models import Room
from rest_framework.response import Response
from ..serializers import RoomSerializer, RoomDetailSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.utils.cache import get_cache_key
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings


class ListRoomPagination(PageNumberPagination):
    page_size = 10  

class ListRoomViewSet(viewsets.GenericViewSet, viewsets.mixins.ListModelMixin):
    """
    a viewset to show all rooms, and your respective link to detail 
    """
    CACHE_PREFIX = 'room-model-list'    

    queryset = Room.objects.availables()
    serializer_class = RoomSerializer
    pagination_class = ListRoomPagination
    permission_classes = [AllowAny]
    
    #@method_decorator(cache_page((int(settings.TIME_CACHE_LIST_VIEWS) * 60), key_prefix=CACHE_PREFIX)) 
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class RoomDetailView(APIView):
    CACHE_PREFIX = 'room-model-list'
    """
    a view only accept retrive to show detail, here use RoomDetailSerializer (have more information)
    """
    permission_classes = [AllowAny]

    def get_object(self):
        id = str(self.kwargs.get('id'))
        objct =  Room.objects.all().filter(id=id).first() 
        return objct
    
    #@method_decorator(cache_page((int(settings.TIME_CACHE_LIST_VIEWS) * 60), key_prefix=CACHE_PREFIX)) 
    def get(self, request, *args, **kwargs): 
        qs = self.get_object()
        serializer = RoomDetailSerializer(
            qs, 
            context={'request': request}
            )
        return Response(serializer.data)
    
    # def retrieve(self, request, *args, **kwargs): #get object with all details
    #     return super().retrieve(request, *args, **kwargs)