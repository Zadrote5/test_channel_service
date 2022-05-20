import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channelService.settings')

app = Celery('channelService')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update_commands': {
        'task': 'main.tasks.check_commands',
        'schedule': crontab(minute='*/1')
    },
}