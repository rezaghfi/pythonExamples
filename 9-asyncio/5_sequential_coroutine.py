import asyncio, time

async def delay(delay_time):
    print(f'{time.ctime()}: Started sleeping for {delay_time} seconds')
    await asyncio.sleep(delay_time)
    print(f'{time.ctime()}: Finished sleeping for {delay_time} seconds')

async def main():
    await delay(2)
    await delay(3)

asyncio.run(main())