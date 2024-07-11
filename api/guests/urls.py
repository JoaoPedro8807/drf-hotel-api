from django.urls import include, path
from .views.user_profile_view import UserProfileViewSet
from .views.user_crud_view import UserCrudViewSet

from .views.user_login_view import LoginView
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

app_name = 'guests'


crud_router = SimpleRouter()



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
        'me/',
        UserProfileViewSet.as_view({
            'get': 'me'
        }),
        name='user_profile'
    ),

    path(
        'user/create/',
        UserCrudViewSet.as_view({
            'post': 'create'
        }),
        name='user_create'
        ),

    path(
        'user/<uuid:id>/edit/',
        UserCrudViewSet.as_view({
            'patch': 'change',
            'delete': 'remove',
            'get': 'retrieve',  
        }),
        name='user_edit'
        )
]

