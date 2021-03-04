#!/usr/bin/env python

# WS client example that gets a number from the server and sends it back in a loop

import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        num = 0
        while True:

            await websocket.send(str(num))

            num = await websocket.recv()
            print(f"< {num}")
            num = int(num)
       

asyncio.get_event_loop().run_until_complete(hello())