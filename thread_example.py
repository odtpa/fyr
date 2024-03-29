import threading
from threading import Thread
from time import sleep


def cal_wt_lock(lock):
    global num

    temp = num
    sleep(0.1)

    num = temp + 1


def cal_w_lock(lock):
    global num
    lock.acquire()

    temp = num
    sleep(0.1)

    num = temp + 1
    lock.release()


def cal_w_semaphore(semaphore):
    global num
    semaphore.acquire()

    temp = num
    sleep(0.1)

    num = temp + 1
    semaphore.release()


def foo(threads, func, arg=None):
    global num
    num = 0
    for i in range(100):
        t = Thread(target=func, args=(arg,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print('result: num = {}'.format(num))


if __name__ == '__main__':
    num = 0
    threads_list = []

    # foo(threads_list, cal_wt_lock)

    # thread_lock = threading.Lock()
    # foo(threads_list, cal_w_lock, thread_lock)
    #
    thread_semaphore = threading.Semaphore(5)
    foo(threads_list, cal_w_semaphore, thread_semaphore)
