import asyncio


async def fetch_page(url, delay=0.01):
    await asyncio.sleep(delay)

    return {
        "url": url,
        "status": "ok",
    }


async def fetch_pages_with_limit(urls, limit=2):
    if limit <= 0:
        raise ValueError("limit must be greater than 0")

    semaphore = asyncio.Semaphore(limit)

    async def fetch_with_semaphore(url):
        async with semaphore:
            return await fetch_page(url)

    tasks = []

    for url in urls:
        task = fetch_with_semaphore(url)
        tasks.append(task)

    return await asyncio.gather(*tasks)
