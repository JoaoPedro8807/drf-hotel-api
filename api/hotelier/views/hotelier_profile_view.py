from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import HotelierUser
from rest_framework import status
from ..serializers.hotelier_profile_serializer import HotelierProfileSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings
User = get_user_model()

class HotelierProfileView(APIView): 
    """
    Endpoint to hotelier get all infos from your hotel and your account. Nedded be logged as hotelier
    """
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return HotelierUser.objects.select_related(
            'auth_user'
            ).prefetch_related(
                'hotel__rooms',
                ).filter(auth_user=self.request.user)
    
    @method_decorator(cache_page((int(settings.TIME_CACHE_LIST_VIEWS) * 60), key_prefix='profile')) 
    def get(self, request, *args, **kwargs):    
        obj = get_object_or_404(
            self.get_queryset()
        )
        try:
            serializer = HotelierProfileSerializer(
                instance=obj,
                context={'request': request}
            )
            return Response(
                serializer.data, 
                status=status.HTTP_200_OK
            )
        
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)
        







