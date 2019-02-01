from nats.aio.client import Client as NATS
import asyncio
import sys

nats = NATS()

async def nats_connect(loop):
    global nats
    try:
        await nats.connect(servers=["nats://0.0.0.0:4222"],
                                connect_timeout=10, dont_randomize=True,
                                allow_reconnect=True, loop=loop,
                                error_cb=error_cb, max_reconnect_attempts=8640,
                                reconnect_time_wait=10
                                )
    except Exception as ermsg:
        print(str(ermsg))
        if str(ermsg) == 'nats: No servers available for connection':
            sys.exit(1)

async def error_cb(error):
    """ Write error to the log file"""
    print("error_callback:" + str(error))


async def nwrite():
    async def request_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print("Received a message on '{subject} {reply}': {data}".format( subject=subject, reply=reply, data=data))
    global nats
    await nats.request("robot",b'initialising', expected=1, timeout=10000, cb=request_handler)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(nats_connect(loop))]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.run_until_complete(nwrite())
    loop.run_forever()
