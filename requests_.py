import asyncio
import time

import aiohttp

import requests
from threading import Thread
from multiprocessing import Process
from numbers_ import measure_time


links = ["https://google.com", "https://amazon.com", "https://microsoft.com"]
iterations = 5


def rq(lnk):
    requests.get(lnk)


@measure_time('sinchro')
def sinchro():
    for _ in range(iterations):
        rq(links[0])
        rq(links[1])
        rq(links[2])


@measure_time('threading')
def threading():
    for _ in range(iterations):
        th1 = Thread(target=rq, args=(links[0], ))
        th2 = Thread(target=rq, args=(links[1], ))
        th3 = Thread(target=rq, args=(links[2], ))
        th1.start()
        th2.start()
        th3.start()
        th1.join()
        th2.join()
        th3.join()


@measure_time('multiprocessing')
def multiprocessing():
    for _ in range(iterations):
        pr1 = Process(target=rq, args=(links[0], ))
        pr2 = Process(target=rq, args=(links[1], ))
        pr3 = Process(target=rq, args=(links[2], ))
        pr1.start()
        pr2.start()
        pr3.start()
        pr1.join()
        pr2.join()
        pr3.join()




async def main():
    st = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(links[0]): pass
        async with session.get(links[1]): pass
        async with session.get(links[2]): pass
        async with session.get(links[0]): pass
        async with session.get(links[1]): pass
        async with session.get(links[2]): pass
        async with session.get(links[0]): pass
        async with session.get(links[1]): pass
        async with session.get(links[2]): pass
        async with session.get(links[0]): pass
        async with session.get(links[1]): pass
        async with session.get(links[2]): pass
        async with session.get(links[0]): pass
        async with session.get(links[1]): pass
        async with session.get(links[2]): pass

    end = time.time()
    print('coroutins:')
    print(f'average time: {(end - st) / iterations}')
    print('------------------------------')


sinchro()
threading()
multiprocessing()
asyncio.run(main())

"""
_________5 iter_______________
sinchro:
average time: 3.1466037750244142
------------------------------
threading:
average time: 1.370477819442749
------------------------------
multiprocessing:
average time: 1.4916419982910156
------------------------------
coroutins:
average time: 1.7278890132904052
------------------------------

________10 iter_______________
sinchro:
average time: 7.1787378787994385
------------------------------
threading:
average time: 2.929059457778931
------------------------------
multiprocessing:
average time: 2.949013423919678
------------------------------
coroutins:
average time: 1.68001708984375
------------------------------

"""