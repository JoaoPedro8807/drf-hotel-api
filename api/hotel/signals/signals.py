# signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.dispatch import receiver
from ..models import  Hotel
from django.core.cache import cache
from django.conf import settings

@receiver(post_save, sender=Hotel)
@receiver(post_delete, sender=Hotel)
def delete_list_hotel_viewset_cache(sender, instance, **kwargs):
    cache_key = 'hotel-model-list' #prefix key on viewset
    keys_pattern = f"views.decorators.cache.cache_page.{cache_key}.*.{settings.LANGUAGE_CODE}.{settings.TIME_ZONE}" #the default format in redis-cache
    cache.delete_pattern(keys_pattern) #delete from redis

