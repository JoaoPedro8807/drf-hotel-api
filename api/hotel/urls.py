from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
    HotelViewSet, 
    ListHotelViewset, 
    HotelDetailViewSet, 
    ListRoomViewSet, 
    RoomViewSet,
    RoomDetailView

    )

app_name = 'hotel'

hotel_router = SimpleRouter()
hotel_router.register(
    '',
    HotelViewSet, #viewset to edit
    basename='hotel_viewset'
)

hotel_router.register(
    'detail',
    HotelDetailViewSet, #view detail
    basename='detail_hotel'
)   
hotel_router.register(
    'list',
    ListHotelViewset, #view list
    basename='list_hotel'
)   
room_router = SimpleRouter()

room_router.register(
    '',
    RoomViewSet,
    basename='room_viewset'

)
room_router.register(
    'list',
    ListRoomViewSet,
    basename='list_room'
)

urlpatterns = [  
    path('hotel/', include(hotel_router.urls)),
    path('room/', include(room_router.urls)),
    path('room/detail/<uuid:id>/', RoomDetailView.as_view(), name='room-detail' )
    #path('room/list/', ListRoomView.as_view(), name='room-list')
]
