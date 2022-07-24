import time
import threading
from threading import Thread


def sleep_me(i):
    print("Поток %i засыпает на 5 секунд." % i)
    time.sleep(5)
    print("Поток %i сейчас проснулся." % i)


for i in range(10):
    th = Thread(target=sleep_me, args=(i,))
    th.start()
    print("Запущено потоков: %i." % threading.active_count())
