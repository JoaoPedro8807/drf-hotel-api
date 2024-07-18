from django.urls import include, path
from .views.user_crud_view import UserCrudViewSet
from .views.guest_profile_view import GuestUserProfile

from .views.user_login_view import LoginView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
app_name = 'guests'
urlpatterns = [
    path(
        'login/',
        LoginView.as_view(),
        name='login'
          ),

    path('login/refresh/', 
         TokenRefreshView.as_view(), 
         name='token_refresh'),

    path('login/verify/', 
         TokenVerifyView.as_view(), 
         name='token_verify'), 

    path(
        'guest/profile/',
        GuestUserProfile.as_view(),
        name='guest-profile'
        ),

    path(
        'create/',
        UserCrudViewSet.as_view({
            'post': 'create'
        }),
        name='user_create'
        ),

    path(
        '<uuid:id>/edit/',
        UserCrudViewSet.as_view({
            'patch': 'change',
            'delete': 'remove',
            'get': 'retrieve',  
        }),
        name='user_edit'
        )
]

