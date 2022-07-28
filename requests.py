# import time
#
# import requests
# from threading import Thread
# from multiprocessing import Process
#
#
# links = ["https://google.com", "https://amazon.com", "https://microsoft.com"]
# iterations = 5
#
#
# def measure_time(way):
#     def decorator(function):
#         def wrapper(*args, **kwargs):
#             print(f'{way}:')
#             st = time.time()
#             result = function(*args, **kwargs)
#             end = time.time()
#             print(f'average time: {(end - st) / iterations}')
#             print('------------------------------')
#             return result
#         return wrapper
#     return decorator
#
#
# def rq(lnk):
#     requests.get(lnk)
#
#
# @measure_time('sinchro')
# def sinchro():
#     for _ in range(iterations):
#         rq(links[0])
#         rq(links[1])
#         rq(links[2])
#
#
# @measure_time('threading')
# def threading():
#     for _ in range(iterations):
#         th1 = Thread(target=rq, args=(links[0], ))
#         th2 = Thread(target=rq, args=(links[1], ))
#         th3 = Thread(target=rq, args=(links[2], ))
#         th1.start()
#         th2.start()
#         th3.start()
#         th1.join()
#         th2.join()
#         th3.join()
#
#
# @measure_time('multiprocessing')
# def multiprocessing():
#     for _ in range(iterations):
#         pr1 = Process(target=rq, args=(links[0], ))
#         pr2 = Process(target=rq, args=(links[1], ))
#         pr3 = Process(target=rq, args=(links[2], ))
#         pr1.start()
#         pr2.start()
#         pr3.start()
#         pr1.join()
#         pr2.join()
#         pr3.join()
#
#
# sinchro()
# threading()
# multiprocessing()
#
# """
# _________5 iter_______________
# sinchro:
# average time: 3.471709430217743
# ------------------------------
# threading:
# average time: 1.3072543740272522
# ------------------------------
# multiprocessing:
# average time: 1.434463620185852
# ------------------------------
#
# ________10 iter_______________
# sinchro:
# average time: 3.404653453826904
# ------------------------------
# threading:
# average time: 1.4470402717590332
# ------------------------------
# multiprocessing:
# average time: 1.3591494798660277
# ------------------------------
#
# """