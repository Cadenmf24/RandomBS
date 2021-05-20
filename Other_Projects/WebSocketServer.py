import asyncio
import websockets


async def main(websocket,path):
    while(True):
        try:
            await websocket.send('Hello There!')
            msg=await websocket.recv()
            print(msg)
        except Exception as e:
            pass


s = websockets.serve(main,'192.168.1.96',1)


asyncio.get_event_loop().run_until_complete(s)
asyncio.get_event_loop().run_forever()


