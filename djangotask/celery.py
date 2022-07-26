from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
import djangoapp.tasks

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangotask.settings')

app = Celery('djangotask')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

#celery Beat settings

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')