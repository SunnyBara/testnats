import nats
import json

nc = None
NATS_SUBJECT = 'foo'
NATS_ADDRESSBOOK = 'addressbook'
NATS_USER = 'user'


async def init_nats():
    global nc
    if nc is None:
        nc = await nats.connect('127.0.0.1:4222', user='b', password='pwd1')
    return nc


async def publish_message(message):
    if nc is None:
        await init_nats()
    msg_str = json.dumps(message)
    await nc.publish(NATS_SUBJECT, msg_str.encode())
    print(f'msg {msg_str}, published')
    await nc.flush()


async def addressbook_handler(message):
    if nc is None:
        await init_nats()
    msg_str = json.dumps(message)
    await nc.publish(NATS_ADDRESSBOOK, msg_str.encode())
    print(f'msg {message}, published')
    await nc.flush()


async def user_handler(message):
    if nc is None:
        await init_nats()
    msg_str = json.dumps(message)
    await nc.publish(NATS_USER + f'/{message.get("sender")}', msg_str.encode())
    print(f'msg {message}, published')
    await nc.flush()
