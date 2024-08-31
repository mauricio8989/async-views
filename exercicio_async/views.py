import httpx
import asyncio
from django.http import HttpResponse


async def fetch_page():
    for num in range(1, 6):
        await asyncio.sleep(1)  # Simulating delay
        print(num)
    async with httpx.AsyncClient() as client:
        response = await client.get('https://example.com')
        print(response)

async def get_page(response):
    loop = asyncio.get_event_loop()
    loop.create_task(fetch_page())
    return HttpResponse("Response do exercício async")