from my_logger import logger

import asyncio
import aiohttp
import requests

async def io_bound(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return response.status
            else:
                raise Exception("error")
    

async def cpu_bound(num):
    return sum([i * i for i in range(num * 1000)])


async def io_bound_main():
    start = asyncio.get_event_loop().time()
    io_input_list = ["https://httpbin.org/get"] * 4
    tasks = [io_bound(url) for url in io_input_list]
    results = await asyncio.gather(*tasks)
    end = asyncio.get_event_loop().time()
    print(end - start)
    logger.info(f"io_bound async_programming: {end - start:.3f} seconds")


async def cpu_bound_main():
    start = asyncio.get_event_loop().time()
    cpu_input_list = [2000, 4000, 6000, 8000]
    tasks = [cpu_bound(cpu_input) for cpu_input in cpu_input_list]
    results = await asyncio.gather(*tasks)
    end = asyncio.get_event_loop().time()
    print(end - start)
    logger.info(f"cpu_bound async_programming: {end - start:.3f} seconds")


if __name__ == '__main__':
    asyncio.run(cpu_bound_main())
    asyncio.run(io_bound_main())