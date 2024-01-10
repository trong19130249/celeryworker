from celery import Celery
import os

from celery.schedules import crontab
from dotenv import load_dotenv

# load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = {
    'send-notification-every-1-seconds': {
        'task': 'notification.tasks.send_notification_task',
        # 5s for testing
        'schedule':5,
        'args': ('Hello World',),
    },
}
app.autodiscover_tasks()
