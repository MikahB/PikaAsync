import asyncio
from listener import ReconnectingExampleConsumer

async def Random():
    while True:
        await asyncio.sleep(2)
        print('[*] Random!')

async def Listener():
    uri = 'amqp://guest:guest@localhost:5672/%2F'
    listener = ReconnectingExampleConsumer(uri)
    listener.run()

async def main():
    random_task = asyncio.create_task(Random())
    asyncio.create_task(Listener())
    await asyncio.gather(random_task)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
