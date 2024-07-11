from django.db import models
import uuid

class AbstractHotelModel(models.Model):        
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True, editable=False)
    

    class Meta:
        abstract = True
        ordering = ['-created_at']
