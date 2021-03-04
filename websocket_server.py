#!/usr/bin/env python

# WS server example that sends back a number 1 higher

import asyncio
import websockets

async def hello(websocket, path):
    while True:
        num = await websocket.recv()
        print(f"< {num}")

        await websocket.send(str(int(num) + 1))

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


