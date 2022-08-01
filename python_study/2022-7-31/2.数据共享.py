# from multiprocessing import Process, Manager, Lock

# def func(i, temp):
#     temp[0] += 1
#     print(i, "---------->", temp[0])
#
#
# if __name__ == '__main__':
#     manager = Manager()
#     temp = manager.list([1, 2, 3])
#     p_list = []
#     for i in range(100):
#         p = Process(target=func, args=(i, temp))
#         p.start()
#         p_list.append(p)
#
#     for p in p_list:
#         p.join()

# 不上锁会出现资源竞争
# -----------------------------------------------------------------

# def func(i, temp):
#     with lock:
#         temp[0] += 100
#         print(i, "---------->", temp[0])
#
# lock = Lock()
# if __name__ == '__main__':
#     manager = Manager()
#     temp = manager.list([1, 2, 3])
#
#     p_list = []
#     for i in range(10):
#         p = Process(target=func, args=(i, temp))
#         p.start()
#         p_list.append(p)
#
#     for p in p_list:
#         p.join()

# ------------------------------------------------
from multiprocessing import Process, Queue
import time
def func(i, q):
    if not q.empty():
        print(i, "--->get value", q.get())
    time.sleep(2)

if __name__ == '__main__':
    q = Queue()
    dct = dict()
    for i in range(6):
        # 往队列里存放数据
        dct["name"]  = i
        q.put(dct)
        p = Process(target=func, args=(i, q))
        p.start()
