from multiprocessing import Pool, current_process
import time



lst = list()
def task(i):
    print(current_process().name, i, "start...")
    time.sleep(2)
    lst.append(i)
    print(lst)
    print(current_process().name, i, "end...")

if __name__ == "__main__":
    # 创建一个进程池，建议进程数和cpu核数一致
    p = Pool(processes=4, maxtasksperchild=2)# maxtasksperchild指定每个进程能执行的最大任务数
    for i in range(20):
        # 进程池接收任务
        p.apply_async(func=task, args=(i, ))

    # 关闭进程池，不接收任务
    p.close()

    # 等待子进程执行完毕
    p.join()
    print("end...")


# 时间 省份 运营商 带宽