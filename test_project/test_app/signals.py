import redis
from django.db.models.signals import post_save
from django.dispatch import receiver
from test_app.models import Dummy

r = redis.Redis(host="localhost", port=6379, db=0)
REDIS_QUEUE = "dummy_events"


@receiver(post_save, sender=Dummy)
def push_to_redis(sender, instance, **kwargs):
    msg = f"Dummy created: {instance.name}"
    r.lpush(REDIS_QUEUE, msg)
    print(f"[Django signal] Message envoyé à Redis: {msg}")
