from ..serializers.profile_serializer import ProfileSerializer
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.shortcuts import get_object_or_404
from rest_framework import status
from ..models.guest_user_model import UserGuest
from ..serializers.profile_serializer import ProfileSerializer
from django.conf import settings



User = get_user_model()

class GuestUserProfile(APIView): 
    """
    endpoint to get guest profile infos, currently bookings, account infos, etc. Nedded be logged as guest
    """
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return UserGuest.objects.select_related(
            'auth_user',
            'booking',
        ).filter(auth_user=self.request.user)
    
    @method_decorator(cache_page((int(settings.TIME_CACHE_LIST_VIEWS) * 60), key_prefix='profile'))
    def get(self, request, *args, **kwargs):    
        obj = get_object_or_404(
            self.get_queryset()
        )
        try:
            serializer = ProfileSerializer(
                instance=obj,
                context={'request': request}
            )
            return Response(
                serializer.data, 
                status=status.HTTP_200_OK
            )
        except Exception as err:
            return Response({'error': str(err)})
        


        



