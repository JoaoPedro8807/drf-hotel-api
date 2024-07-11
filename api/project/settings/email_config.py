import os
import certifi

#the lastest version of djnago rais error when set default mailBackend
EMAIL_BACKEND = 'booking.backends.email_backend.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', '')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', True)
EMAIL_USE_SSL = False    
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '#')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '#')

print('email configs: ', EMAIL_BACKEND, EMAIL_HOST, EMAIL_PORT, EMAIL_USE_TLS, EMAIL_HOST_USER,
      EMAIL_HOST_PASSWORD)  