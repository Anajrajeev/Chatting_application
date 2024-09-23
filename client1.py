import asyncio
import websockets
async def connect():
        async with websockets.connect("ws://localhost:5050") as websocket:
            message=input("enter your message")
            await websocket.send(message)
            response = await websockets.recv()
            print(f"Response from server: {response}")
asyncio.run(connect())
