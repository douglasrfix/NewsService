import sys
import asyncio
import aioipfs
async def pubsub_serve(topic):
    async with aioipfs.AsyncIPFS() as cli:
        async for message in cli.pubsub.sub(topic):
            print('Received message from', message['from'])
            await cli.pubsub.pub(topic, message['data'])

loop = asyncio.get_event_loop()
loop.run_until_complete(pubsub_serve(sys.argv[1:]))
loop.close()