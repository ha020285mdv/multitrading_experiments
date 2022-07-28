import asyncio
import time
from threading import Thread
from multiprocessing import Pool, BoundedSemaphore
from multiprocessing import Process


def measure_time(way):
    def decorator(function):
        def wrapper(*args, **kwargs):
            print(f'{way}:')
            st = time.time()
            result = function(*args, **kwargs)
            end = time.time()
            print(f'average time: {(end - st) / iterations}')
            print('------------------------------')
            return result
        return wrapper
    return decorator


p = 1000 * 1000 * 10
args = [(2, p), (3, p), (5, p)]
iterations = 5


def power(num, p):
    rez = num ** p
    return rez


@measure_time('sinchro')
def sinchro():
    for _ in range(iterations):
        for n, s in args:
            power(n, s)


@measure_time('threading')
def threading():
    for _ in range(iterations):
        for arg in args:
            th = Thread(target=power, args=arg)
            th.start()


@measure_time('threading(semaphore)')
def threading_with_semaphore():
    semaphore = BoundedSemaphore(value=3)

    def handler(num, p):
        with semaphore:
            power(num, p)

    for _ in range(iterations):
        clients = [Thread(target=handler, args=(num, p)) for num, p in args]
        for b in clients:
            b.start()


@measure_time('multiprocessing')
def multiprocessing():
    for _ in range(iterations):
        p1 = Process(target=power, args=args[0])
        p2 = Process(target=power, args=args[1])
        p3 = Process(target=power, args=args[2])
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()


@measure_time('multiprocessing (with pool)')
def multiprocessing_with_pool():
    pool = Pool(processes=3)
    for i in range(iterations):
        pool.starmap(power, args)


async def power_coroutine(num, p):
    rez = num ** p
    return rez


async def main():
    st = time.time()
    await asyncio.gather(
        power_coroutine(*args[0]),
        power_coroutine(*args[1]),
        power_coroutine(*args[2]),

        power_coroutine(*args[0]),
        power_coroutine(*args[1]),
        power_coroutine(*args[2]),

        power_coroutine(*args[0]),
        power_coroutine(*args[1]),
        power_coroutine(*args[2]),

        power_coroutine(*args[0]),
        power_coroutine(*args[1]),
        power_coroutine(*args[2]),

        power_coroutine(*args[0]),
        power_coroutine(*args[1]),
        power_coroutine(*args[2]),
    )
    end = time.time()
    print('coroutins:')
    print(f'average time: {(end - st)/5}')
    print('------------------------------')



sinchro()
threading()
threading_with_semaphore()
multiprocessing()
multiprocessing_with_pool()
asyncio.run(main())


#############################################################
"""
          100 000 000
______________________________
sinchro:
average time: 204.22850608825684
------------------------------
threading:
average time: 204.9342439174652
------------------------------
threading(semaphore):
average time: 205.86898803710938
------------------------------
multiprocessing:
average time: 136.35200023651123
------------------------------
multiprocessing (with pool):
average time: 134.47210884094238
------------------------------
coroutins:
average time: 203.478124666214
------------------------------

          10 000 000
______________________________
sinchro:
average time: 5.377600193023682
------------------------------
threading:
average time: 5.416457891464233
------------------------------
threading(semaphore):
average time: 5.669945240020752
------------------------------
multiprocessing:
average time: 3.4548962116241455
------------------------------
multiprocessing (with pool):
average time: 3.7139923572540283
------------------------------
coroutins:
average time: 5.3209587097167965
------------------------------

          1 000 000
______________________________
sinchro:
average time: 0.13901448249816895
------------------------------
threading:
average time: 0.14002609252929688
------------------------------
threading(semaphore):
average time: 0.14545607566833496
------------------------------
multiprocessing:
average time: 0.09177708625793457
------------------------------
multiprocessing (with pool):
average time: 0.0968179702758789
------------------------------
coroutins:
average time: 0.13803958892822266
------------------------------

"""