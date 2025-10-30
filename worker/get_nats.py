import asyncio
import nats

NATS_SUBJECT = "foo"


async def message_handler(msg):
    print(f"[read_from_nats] Reçu sur NATS: {msg.data.decode()}")


async def main():
    nc = await nats.connect("demo.nats.io")
    await nc.subscribe(NATS_SUBJECT, cb=message_handler)
    print("Consumer NATS démarré...")

    while True:
        await asyncio.sleep(1)


asyncio.run(main())
