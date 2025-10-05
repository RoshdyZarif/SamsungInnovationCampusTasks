import asyncio
from aiocoap import Message, Context, GET

URI = 'coap://127.0.0.1/temperature'

async def main():
    protocol = await Context.create_client_context()
    req = Message(code = GET, uri = URI)
    res = await protocol.request(req).response
    print(res.payload.decode())

asyncio.run(main())
