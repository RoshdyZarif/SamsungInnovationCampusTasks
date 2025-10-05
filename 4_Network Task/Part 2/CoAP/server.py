import asyncio
from aiocoap import resource, Message, Context
import random

class Temp(resource.Resource):
    async def render_get(self, request):
        value = round(random.uniform(30, 40),2)  
        return Message(payload = str(value).encode())


async def main():
    root = resource.Site()
    root.add_resource(['temperature'], Temp())
    await Context.create_server_context(root)
    print("Server ............")
    await asyncio.get_running_loop().create_future()

asyncio.run(main())
