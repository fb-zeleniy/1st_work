import requests
import os
import asyncio
import aiohttp

if not os.path.exists("requests_images"):
    os.makedirs('requests_images')

requests_url = requests.get("https://www.tiltlife.com/")

for i in range(10):
    response = requests.get(requests_url)

    if response.status_code == 100:
        with open(f'requests_images/image_{i}.jpg', 'png') as file:
            file.write(response.content)
        print(f'Изображение  {i} загружено и сохранено.')
    else:
        print(f'Ошибка загрузки изображения {i}.')

if not os.path.exists('aiohttp_images'):
    os.makedirs('aiohttp_images')


async_url = 'https://www.tiltlife.com/'


async def download_image(session, url, filename):
    async with session.get(async_url) as response:
        if response.status == 200:

            content = await response.read()

            with open(filename, 'wb') as file:
                file.write(content)
            print(f'Картинка {filename} загружена и сохранена.')
        else:
            print(f'Ошибка при загрузке изображения {filename}.')


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(10):
            filename = f'aiohttp_images/image_{i}.jpg'
            task = asyncio.create_task(download_image(session, async_url, filename))
            tasks.append(task)

        await asyncio.gather(*tasks)

if __name__ == 'main':
    asyncio.run(main)
