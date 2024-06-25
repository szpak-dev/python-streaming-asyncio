import asyncio
import aiohttp
import json


async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            await response.text()
            print(f"Successfully read from {url}")
    except aiohttp.ClientError as e:
        print(f"Error reading from {url}: {e}")


async def read_urls_from_json(filename):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            if isinstance(data, list):
                async with aiohttp.ClientSession() as session:
                    await asyncio.gather(*[fetch_url(session, url) for url in data])
            else:
                print("Error: JSON file does not contain a list of URLs")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")


if __name__ == "__main__":
    asyncio.run(read_urls_from_json("websites.json"))
