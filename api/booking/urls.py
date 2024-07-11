from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .import views

app_name = 'booking'

router = SimpleRouter()
# router.register(
#     'teste',
#     views.TesteViewSet,
#     basename='teste'
# )
router.register(
    '',
    views.BookingViewSet,
    basename='booking_viewset'

)
print('URLS DO TESTE: ', router.urls)

urlpatterns = [  
    path('teste', views.TesteViewSet.as_view({
        'post': 'post'
    })),
    path('', include(router.urls))
]
