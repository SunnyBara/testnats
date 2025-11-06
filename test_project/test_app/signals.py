import asyncio

from django.db.models.signals import post_save
from django.dispatch import receiver
from test_app.models import Geo
from test_app.nats import publish_message, addressbook_handler, user_handler
from test_app.views import addressbook_signal, user_signal


@receiver(post_save, sender=Geo)
async def send_nats_data(sender, instance, **kwargs):
    data = {'name': instance.name, 'color': instance.color}
    asyncio.create_task(publish_message(data))


@receiver(addressbook_signal)
async def signal_addressbook_handler(sender, instance=None, **kwargs):
    asyncio.create_task(addressbook_handler({'message': 'addressbook signal'}))


@receiver(user_signal)
async def signal_user_handler(sender, instance=None, **kwargs):
    asyncio.create_task(
        user_handler({'message': 'user signal', 'sender': f'{sender}'})
    )
