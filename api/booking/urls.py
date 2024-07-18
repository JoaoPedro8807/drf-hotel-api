from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .import views

app_name = 'booking'

router = SimpleRouter()

router.register(
    '',
    views.BookingViewSet,
    basename='booking_viewset'
)

urlpatterns = [  
    path('', include(router.urls))
]
