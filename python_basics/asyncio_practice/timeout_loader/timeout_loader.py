import asyncio


async def load_service_data(service_name, delay=0.01):
    await asyncio.sleep(delay)

    return {
        "service": service_name,
        "status": "loaded",
    }


async def load_service_data_with_timeout(service_name, delay=0.01, timeout=0.05):
    try:
        return await asyncio.wait_for(
            load_service_data(service_name, delay),
            timeout=timeout,
        )
    except asyncio.TimeoutError:
        return {
            "service": service_name,
            "status": "timeout",
        }


async def load_multiple_services(services, timeout=0.05):
    tasks = []

    for service in services:
        task = load_service_data_with_timeout(
            service["name"],
            delay=service["delay"],
            timeout=timeout,
        )
        tasks.append(task)

    return await asyncio.gather(*tasks)