from django.apps import AppConfig

class HotelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    def ready(self) -> None:
        ready =  super().ready()
        import hotel.signals
        return ready
    name = 'hotel'
