import time
import asyncio
import requests



async def func1():
    print("func 1")
    url = 'https://wallpapercave.com/wp/wp11383551.jpg'
    r = requests.get(url, allow_redirects=True)
    open('vegeta.png', 'wb').write(r.content)

    return "nikul"

async def func2():
    print("func 2")
    url = 'https://pbs.twimg.com/media/EzJf5v_VkAMcRXr?format=jpg&name=4096x4096'
    r = requests.get(url, allow_redirects=True)
    open('ssj4vegeta.png', 'wb').write(r.content)


async def func3():
    print("func 3")
    url = 'https://images8.alphacoders.com/135/1355096.jpeg'
    r = requests.get(url, allow_redirects=True)
    open('goku.png', 'wb').write(r.content)

async def main():
    # await func1()
    # await func2()
    # await func3()
    # return 3
    L = await asyncio.gather(
         func1(),
         func2(),
         func3()
    )
    print(L)

asyncio.run(main())