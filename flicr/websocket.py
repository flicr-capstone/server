import asyncio
import json
import websockets

from .payloadtype import PayloadType
from .uart import Uart

uart = None


async def triage(ws, _path):
    while True:
        payload = json.loads(await ws.recv())
        payload_type = PayloadType(payload["type"])
        if payload_type == PayloadType.GREET:
            await greet(ws, payload["msg"])
        if payload_type == PayloadType.KEY_EVENT:
            await receiveKeyEvent(ws, payload["msg"])


async def send(ws, payload_type, msg):
    await ws.send(json.dumps({"type": payload_type, "msg": msg}))


async def greet(ws, greeting):
    print(f"< {greeting}")
    response = {"greeting": f"Hello {greeting['name']}!"}
    await send(ws, PayloadType.GREET, response)
    print(f"> {response}")


async def receiveKeyEvent(_ws, keyEvent):
    print(f"< {keyEvent}")
    uart.write_str_ln(keyEvent)


def run():
    print("Starting WebSocket Server")
    global uart
    uart = Uart()
    start_server = websockets.serve(triage, "0.0.0.0", 8080)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
