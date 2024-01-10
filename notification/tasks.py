from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from core.celery import app


@shared_task
def send_notification_task(message):

    channel_layer = get_channel_layer()
    print("channel_layer: ", channel_layer)
    async_to_sync(channel_layer.group_send)(
        "notifications",
        {
            "type": "send_notification",
            "message": message
        }
    )
    # gửi lên broadcast group notifications

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(1.0, send_notification_task.s("Hello World"), name="Send notification every 1 seconds")
