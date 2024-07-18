from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    #api
    path('admin/', admin.site.urls),
    path('user/', include('guests.urls')), #generic user services is 'user/'  (guests_app)   and  generic guests services is '/guests' (guest_app)
    path('', include('hotel.urls')),
    path('booking/', include('booking.urls')),
    path('hotelier/', include('hotelier.urls'))
]
