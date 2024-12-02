import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        delay = 1 / power
        await asyncio.sleep(delay)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Vasya', 5))
    task2 = asyncio.create_task(start_strongman('Kolya', 3))
    task3 = asyncio.create_task(start_strongman('Denis', 4))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())