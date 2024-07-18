from rest_framework import permissions

class BookingPermission(permissions.BasePermission): 
    """
    check if user auth is the hotelier or guest on booking instance, then he can update the booking
    """
    def has_object_permission(self, request, view, obj):
        method = request.method.upper()
        print('comparando', obj.guest.id, 'com', request.user.guest_user.id)
        if method == 'DELETE': #delete só hotelier 
            return obj.guest.id == request.user.guest_user.id 
           
        elif method == 'GET': #get pode pelo hotelier e guest
            return  obj.guest.id == request.user.guest_user.id or obj.room.hotel.hotelier == request.user.especific_user
        
        return True

    def has_permission(self, request, view):
        return super().has_permission(request, view)
    
    
