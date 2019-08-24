from flask import Flask
import asyncio
import websockets

app = Flask(__name__)


@app.route('/')
def index():
	return "Hello World!"


async def hello(websocket, path):
	while True:
		name = await websocket.recv()

		print(f"< {name}")

		greeting = f"Hello {name}!"

		await websocket.send(greeting)
		print(f"> {greeting}")


def main():
	start_server = websockets.serve(hello, "localhost", 8080)

	asyncio.get_event_loop().run_until_complete(start_server)
	asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
	main()
