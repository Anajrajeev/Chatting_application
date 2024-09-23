import websockets
import asyncio
print("server is running..........")
async def receive(websocket, path):
    print("connected to client.......")
    try:
        async for message in websocket:
            print(f"Received message from client: {message}")
            await websocket.send(f"Message received: {message}")
    except websockets.ConnectionClosed as e:
        print("Connection closed", e)
async def start():
    server=await websockets.serve(receive,"localhost",5050)
    await server.wait_closed()
asyncio.run(start())
asyncio.get_event_loop().run_forever()