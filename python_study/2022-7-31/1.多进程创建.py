'''
    进程的组成：
        进程控制块PCB、数据段、正文段
    基本状态：就绪状态、运行状态、阻塞状态
'''
'''
    一个今晨个都是由另一个进程创建的
    linux中：
    pid为0的进程：是所有进程的主进程
    pid为1的进程：创建用户进程
    pid为2的进程：创建系统进程
'''
# import os, time
#
# pid = os.fork()

#父进程运行时pid为子进程的pid，子进程运行时这个pid就为0
# print("outerside pid is :", pid)
#
# if pid == 0:
#     print("child precess")
#     time.sleep(60)
#     print("child pid is :", os.getpid())
#     print("child-parent pid is:", os.getppid())
# else:
#     print("parent precess")
#     time.sleep(60)
#     print("parent pid is :", os.getpid())

'''
    父进程提前退出，子进程的ppid会变为1，这个进程称为孤儿进程
    子进程提前结束，父进程没有响应，父进程没有调用wait或者waitpid去获取子进程的状态
    那么子进程的进程描述符就会依然保存在系统中，这种进程称之为僵尸进程
'''

from multiprocessing import Process, current_process
import time

lst = list()
def task(i):
    print(current_process().name, i, "start...")
    time.sleep(2)
    lst.append(i)
    print(lst)
    print(current_process().name, i, "end...")

# if __name__ == "__main__":
#     for i in range(4):
#         p = Process(target=task, args=(i,))
#         p.start()

# 各个进程都拥有一份数据，相互隔离

# 自定义进程类

class Myprocess(Process):
    def __init__(self, i):
        super().__init__()
        self.i = i
    def run(self):
        task(self.i)

if __name__ == "__main__":
    for i in range(4):
        p = Myprocess(i)
        p.start()