import asyncio


async def load_profile(username, delay=0.01):
    await asyncio.sleep(delay)

    if not username:
        raise ValueError("username is required")

    return {
        "username": username,
        "status": "loaded",
    }


async def load_profile_safe(username):
    try:
        return await load_profile(username)
    except ValueError as error:
        return {
            "username": username,
            "status": "error",
            "error": str(error),
        }


async def load_profiles(usernames):
    tasks = []

    for username in usernames:
        task = asyncio.create_task(load_profile_safe(username))
        tasks.append(task)

    return await asyncio.gather(*tasks)
