import websockets
import asyncio


async def listen():
    url="ws://192.168.1.96:1"

    async with websockets.connect(url) as pel:
        msg=await pel.recv()
        print(msg)



asyncio.get_event_loop().run_until_complete(listen())