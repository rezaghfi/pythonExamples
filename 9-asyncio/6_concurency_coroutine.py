import asyncio, time

async def delay(delay_time):
    print(f'{time.ctime()}: Started sleeping for {delay_time} seconds')
    await asyncio.sleep(delay_time)
    print(f'{time.ctime()}: finished sleeping for {delay_time} seconds')

async def main():
    #non-blocking
    delay_7 = asyncio.create_task(delay(7))
    delay_2 = asyncio.create_task(delay(2))
    delay_4 = asyncio.create_task(delay(4))

    print(type(delay_2))
    #await asyncio.sleep(10)

    #blocking
    await delay_7
    await delay_2
    await delay_4

asyncio.run(main())