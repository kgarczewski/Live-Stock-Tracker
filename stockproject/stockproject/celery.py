from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
# from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockproject.settings')

app = Celery('stockproject')
app.conf.enable_utc = False
app.conf.update(timezone='Poland/Warsaw')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'every-5-seconds': {
        'task': 'mainapp.tasks.get_coins_data',
        'schedule': 5,
    },
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
