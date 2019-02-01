import asyncio
from nats.aio.client import Client as NATS

async def run(loop):
    nc = NATS()

    await nc.connect("nats://0.0.0.0:4222", loop=loop)

    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data
        print("Received a message on '{subject} {reply}': {data}".format( subject=subject, reply=reply, data=data))
        await nc.publish(reply, data)


    # Simple publisher and async subscriber via coroutine join the queued-handler queue. Only one handler in the queue will receive a message
    await nc.subscribe("robot", 'queued-handler', cb=message_handler)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.run_forever()
    loop.close()