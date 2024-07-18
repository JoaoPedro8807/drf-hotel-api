from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import HotelierProfileView

app_name = 'hotel'

urlpatterns = [  
    path(
        'profile/',
        HotelierProfileView.as_view(),
        name='hotelier-profile'
        )
]
