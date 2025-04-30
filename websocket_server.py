import asyncio
import websockets
import subprocess
import json

async def handle_connection(websocket, path):
    try:
        async for message in websocket:
            schedule = json.loads(message)
            on_time = schedule['onTime']
            off_time = schedule['offTime']
            
            # Publish to MQTT
            subprocess.run([
                'mosquitto_pub',
                '-t', 'light/schedule',
                '-m', json.dumps({'on': on_time, 'off': off_time})
            ])
            
            await websocket.send(f"Schedule set: ON at {on_time}, OFF at {off_time}")
            
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {e}")

async def main():
    server = await websockets.serve(handle_connection, "localhost", 8765)
    print("WebSocket server running on ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())