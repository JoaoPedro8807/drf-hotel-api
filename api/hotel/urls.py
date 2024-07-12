from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from .views import  HotelViewSet, ListHotelViewset, HotelDetailViewSet

app_name = 'hotel'

router = SimpleRouter()
#list_router = SimpleRouter()
router.register(
    '',
    HotelViewSet,
    basename='hotel_viewset'
)
router.register(
    'list',
    ListHotelViewset,
    basename='list_hotel'
)   
router.register(
    'detail',
    HotelDetailViewSet,
    basename='detail_hotel'
)


print('URLS DO HOTEL: ', router.urls)

urlpatterns = [  
    path('', include(router.urls))
    #path('list', include(list_router.urls))
]
