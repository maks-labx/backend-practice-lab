import asyncio


async def load_profile(username, delay=0.01):
    await asyncio.sleep(delay)

    return {
        "username": username,
        "status": "loaded",
    }


async def load_profiles(usernames):
    tasks = []

    for username in usernames:
        task = load_profile(username)
        tasks.append(task)

    return await asyncio.gather(*tasks)