# meu_app/views.py
from django.utils import timezone
from datetime import timedelta
from datetime import datetime
from rest_framework import viewsets
from ..models import  Booking
from ..serializers.booking_serizlier import BookingSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..tasks import post_booking
from rest_framework.response import Response

#from .models import Booking
#from ..tasks import finalizar_booking

class TesteViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]


    def post(self, request, *args, **kwargs):
        eta = datetime.now() + timedelta(hours=3, minutes=1)
        print(f'agora é {datetime.now()}, e a tarefa foi agendada para {eta}')
        teste = post_booking.apply_async(eta=eta)
        #teste.get()             
        return Response({'result': 'ok'})





