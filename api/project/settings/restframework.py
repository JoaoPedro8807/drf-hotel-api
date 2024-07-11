
from datetime import timedelta

from project import settings


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination', 
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer'
    # )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,                                                              
    "UPDATE_LAST_LOGIN": False,
    "SIGNING_KEY": str(settings.SECRET_KEY_JWT),
    "AUTH_HEADER_TYPES": ("Bearer",),

}                                        

print('JWT CONFIG: ', SIMPLE_JWT)