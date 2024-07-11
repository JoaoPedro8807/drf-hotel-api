import os
from celery import Celery
from django.conf import settings
from datetime import timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

app = Celery("project")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.timezone = 'America/Sao_Paulo'

app.conf.beat_schedule = {
    "every_thirty_seconds": {
        "task": "booking.tasks.thirty_second_func",
        "schedule": timedelta(seconds=30),
    },
}

app.autodiscover_tasks()



