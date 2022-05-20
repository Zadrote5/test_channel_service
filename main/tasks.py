from channelService.celery import app
from django.core.management import call_command


@app.task
def check_commands():
    call_command('update_orders')
