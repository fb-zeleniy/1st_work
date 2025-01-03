import time
import aiohttp
import asyncio

async def fetch_url(session, url):
    """Fetch content from a URL asynchronously."""
    async with session.get(url) as response:
        return await response.text()

async def download_urls(urls):
    """Download content from a list of URLs asynchronously."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 101)]

    # Measure time for asynchronous download
    start_time = time.time()
    asyncio.run(download_urls(urls))
    elapsed_time = time.time() - start_time
    print(f"Execution time: {elapsed_time:.2f} seconds")
