from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from manipulationFunctions import *
from AICalling import callAI
from pydantic import BaseModel

app = FastAPI()


class CommandRequest(BaseModel):
  command: str

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


@app.post("/command")
async def websocket_endpoint(payload: CommandRequest):
    
    data = payload
    print(f"Received: {data}")

    # Echo acknowledgment back to the sender
    # Process raw text into structured intent
    parsed_command = data.command

    print(parsed_command)

    full_command = callAI(parsed_command)
    if(full_command.device == "front_door_lock"):
        if full_command.action == "unlock":
            # Manipulation functions unlock
            print("unlocking")
            unlockDoor()
        elif full_command.action == "lock":
            # Manipulation functions lock
            print("locking")
            lockDoor()
    elif(full_command.device == "fan"):
        if full_command.action == "fan_on":
            # Manipulation functions fan on
            print("unlocking")
            fanOn()
        elif full_command.action == "fan_off":
            # Manipulation functions fan off
            print("locking")
            fanOff()