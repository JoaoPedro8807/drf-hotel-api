from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist
from ..models.hotel_model import Hotel
from hotelier.models.hotelier_user_model import HotelierUser

class IsHotelOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(request.user, 'hotelier_user'):
            return obj.hotelier == request.user.hotelier_user
        
        return False        
    def has_permission(self, request, view):
        return super().has_permission(request, view)    