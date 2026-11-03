from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from manipulationFunctions import *
from AICalling import callAI

app = FastAPI()


class ConnectionManager:

    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)

    def see_connections(self):
        return self.active_connections


manager = ConnectionManager()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    print(f"Client connected: {websocket.client}")

    try:
        while True:
            # Keeps socket open and blocks until a new message arrives
            data = await websocket.receive_text()
            print(f"Received: {data}")

            # Echo acknowledgment back to the sender
            await websocket.send_text(f"Received message: {data}")

            # Process raw text into structured intent
            parsed_command = data

            
            if parsed_command == "unlock":
                # Manipulation functions unlock
                unlockDoor()
            elif parsed_command == "lock":
                # Manipulation functions lock
                lockDoor()
                    

    except WebSocketDisconnect:
        print(f"Client disconnected: {websocket.client}")
        manager.disconnect(websocket)
    except Exception as e:
        print(f"Error occurred: {e}")
        manager.disconnect(websocket)
