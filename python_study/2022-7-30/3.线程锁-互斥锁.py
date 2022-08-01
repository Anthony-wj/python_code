import threading
import time

num = 0

def sum_num(i):
    lock.acquire()  # 加锁
    global num
    time.sleep(1)
    num += i
    print(num)
    lock.release()  # 释放锁

    # 等效于如下代码
    # with lock:
    #     global num
    #     time.sleep(1)
    #     num += i
    #     print(num)


t_list = []

# lock = threading.Lock()  # 创建一个锁对象
#
# for i in range(6):
#     t = threading.Thread(target=sum_num, args=(i, ))
#     t_list.append(t)
#     t.start()
# for t in t_list:
#     t.join()




'''
    访问公共资源时需要加锁
        Lock()/RLock：普通锁（互斥锁）
        解决资源争用，数据读取不一致等
        • Semaphore ：信号量
        最多允许同时N个线程执行内容
        • Event: 事件锁
        根据状态位，决定是否通过事件
        • Condition: 条件锁
    互斥锁有Lock 和 RLock
    threading.Lock() 有__enter__和__exit__方法，说明这是一个上下文管理器
    lock = threading.Lock()  # 创建一个锁对象
    lock.acquire()  # 加锁
    lock.release()  # 释放锁
'''

'''
    LOCK和RLOCK
    LOCK不能嵌套使用，嵌套会导致死锁。acquire和release必须成对存在
    RLOCK是可以嵌套的
    
'''
# lk = threading.RLock()
# print("start...")
# lk.acquire()
# print("get acquire 1...")
# lk.acquire()
# print("get acquire 2...")
#
# lk.release()
# print("release acquire 2...")
# lk.release()
# print("release acquire 1...")

# ------------------------------------

# lock = threading.BoundedSemaphore(2)  #创建一个锁对象，给了2把钥匙
# for i in range(6):
#     t = threading.Thread(target=sum_num, args=(i,))
#     t_list.append(t)
#     t.start()
#
# for t in t_list:
#     t.join()

# ---------------------------------------------------
# GIL全程Global Intepreter Lock(全局解释器锁)
# GIL和python语言没有任何关系，只是因为历史原因导致在官方推荐的解释器Cpython中遗留的问题
# 每个线程在执行的过程中都需要先获取GIL，保证同一时刻只有一个线程可以执行代码
# 阻塞的线程会释放GIL锁
# 由于GIL锁的存在，所以多线程不适合计算型任务，而更适合IO型任务
# GIL不能保证共享资源的竞争
# 一个GIL只存在于一个进程中，可以多用多进程技术来替代

'''
线程互斥锁和 GIL 的区别
GIL 和线程互斥锁的粒度是不同的，GIL 是 Python 解释器级别的互斥，保证的是解释器级别共享资源的一致性，而线程互斥锁则是代码级（或用户级）的互斥，保证的是 Python 程序级别共享数据的一致性
'''



# linux下的五中IO模型
