import aiohttp
import asyncio
from bs4 import BeautifulSoup
import time

TARGET_PAGE_URL = "https://en.wikipedia.org/wiki/Adolf_Hitler"
MAX_HOPS = 5
cache = {}
semaphore = asyncio.Semaphore(100)

async def fetch_links(session, page):
    async with semaphore:
        if page in cache:
            return cache[page]

        try:
            async with session.get(page) as response:
                html = await response.text()
        except aiohttp.ClientError:
            return []

        soup = BeautifulSoup(html, 'lxml')
        base_url = page[:page.find('/wiki/')]
        links = [base_url + a['href'] for a in soup.select('p a[href]') if a['href'].startswith('/wiki/')]

        cache[page] = links
        return links

def have_page(links):
    return TARGET_PAGE_URL in links

async def find_path(page, hops=0, path=[]):
    async with aiohttp.ClientSession() as session:
        links = await fetch_links(session, page)
        path.append(page)

        if hops > MAX_HOPS:
            print("Not found")
            for task in asyncio.all_tasks():
                task.cancel()
            return []

        if have_page(links):
            path.append(TARGET_PAGE_URL)
            print("Found! Path:", ' -> '.join(path))
            for task in asyncio.all_tasks():
                task.cancel()
            return path
        else:
            hops += 1
            tasks = [asyncio.create_task(find_path(link, hops, path.copy())) for link in links]
            await asyncio.gather(*tasks)

async def main():
    try:
        await find_path(START_URL)
    except asyncio.CancelledError:
        pass

START_URL = input("Input start url: ")
print("Searching for Hitler...")
start_time = time.time()
asyncio.run(main())
end_time = time.time()
print("Search completed in {:.2f} seconds.".format(end_time - start_time))
input("Exit")
