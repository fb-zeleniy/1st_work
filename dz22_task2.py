import aiohttp
import asyncio

URL = "https://jsonplaceholder.typicode.com"

async def fetch_json():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            data = await response.json()
            return data

async def main():
    json_data = await fetch_json()
    print(json_data[:5])

if __name__ == "__main__":
    asyncio.run(main())