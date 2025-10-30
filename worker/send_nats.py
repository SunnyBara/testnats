# send_to_nats.py
import asyncio
import redis
import nats

REDIS_QUEUE = "dummy_events"
NATS_SUBJECT = "foo"

r = redis.Redis(host="localhost", port=6379, db=0)
nc = None


async def main():
    nc = await nats.connect("demo.nats.io")

    print("Worker Redis → NATS démarré...")
    while True:
        _, msg = r.brpop(REDIS_QUEUE)
        msg = msg.decode()
        await nc.publish(NATS_SUBJECT, msg.encode())
        await nc.flush()
        print(f"[send_to_nats] Envoyé sur NATS: {msg}")


asyncio.run(main())
