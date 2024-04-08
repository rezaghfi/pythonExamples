import asyncio, time

#coroutine
async def main():
    print(f'{time.ctime()}: coroutine started!')
    #after await command: coroutine , task , future
    await asyncio.sleep(1)
    print(f'{time.ctime()}: coroutine endted')
# event loop implement with run API in asyncio
asyncio.run(main())