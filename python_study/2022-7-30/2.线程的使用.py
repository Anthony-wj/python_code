'''
    线程：被称为轻量级进程，是cpu调度的基本单位
    组成：线程ID、当前指令指针(PC)、寄存器集合、堆栈组成
    多线程：在单个程序中同时运行多个线程完成不同的工作
'''

import threading
import requests
import time

def runtime(func):
    def _cost(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"当前函数运行时间为:{end - start}")
        return result
    return _cost

def get_content(url):
    res = requests.get(url).text
    time.sleep(0.5)
    print("get text")

# @runtime
# def main():
#     for i in range(5):
#         get_content(
#             "https://www.baidu.com"
#         )
#
# main()

# -----------------------------------------------------

url = "https://www.baidu.com"
# @runtime
# def main():
#     t_list = []
#     for i in range(5):
#         # 创建线程
#         # target -->指定要传入的方法的名字， 要做什么
#         # args -->指定方法要传入的参数  元祖类型
#         t = threading.Thread(target=get_content, args=(url,))
#         t_list.append(t)
#         print(t.name)
#         t.is_alive()
#         t.start() # 启动线程
#
#     for t in t_list:
#         t.join() #join 阻塞当前环境上下文，直到t的线程执行完成
# main()
# --------------------------------------------------------
# @runtime
# def main():
#     for i in range(5):
#         # 创建线程
#         # target -->指定要传入的方法的名字， 要做什么
#         # args -->指定方法要传入的参数  元祖类型
#         t = threading.Thread(target=get_content, args=(url,))
#         t.start() # 启动线程
#         t.join() #
#
# main()
# 当前函数运行时间为:2.913649320602417
# 并不能在主线程创建线程的同时也是用t.join()，因为主线程每创建一个线程，t.join()就会阻塞主线程，
# 即在线程没有执行完之前，主线程不能创建下一个线程。

'''
    t.name 获取或设置线程的名字
    t.getName()/setName(name)获取/设置线程名
    t.is_alive()
    t.run() 线程被cpu调度后自动执行线程对象的run方法
    t.start() 线程准备就绪，等待cpu调度，start会自动调用t.run()
    [parameter] 表示可选参数
    t.join([timeout]) 阻塞当前上下文环境的线程，直到调用此方法的线程结束后者timeout
    t.setDaemon(bool) 设置为后台线程(默认前台线程False)
        • 如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程和后台线程均停止
        • 如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
'''

# ----------------------------------------------------------------------------
# 自定义线程类
# class Mythread(threading.Thread):
#     def __init__(self, url):
#         super().__init__()
#         self.url = url
#
#     def run(self):
#         res = requests.get(self.url).text
#         time.sleep(0.5)
#         print("running.....")
#
# @runtime
# def main():
#     print("start...")
#     t_list = []
#     for i in range(5):
#         t = Mythread(url)
#         t_list.append(t)
#         t.start()
#     for t in t_list:
#         t.join()
#
# if __name__ == '__main__':
#     main()

# -----------------------------------------------------
# @runtime
# def main():
#     t_list = []
#     for i in range(5):
#         t = threading.Thread(target=get_content, args=(url,))
#         t_list.append(t)
#         t.start()
#
#     for t in t_list:
#         t.join()
#
# main()
