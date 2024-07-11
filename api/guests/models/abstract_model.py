from django.db import models
import uuid
from django.utils import timezone

class BaseAbstractModel(models.Model):
    """
    A model to add uuid to Model
    the reason is because uuid conflit with orders default django tables and uuid model 
    costs a lot to Postgres transitions
    """
    id = models.BigAutoField(primary_key=True, editable=False)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True, editable=False)


    class Meta:
        abstract = True
        ordering = ['-created_at']


