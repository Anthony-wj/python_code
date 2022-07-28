'''
    psutil: process and system utilities
    能够轻松实现获取系统运行的进程和系统利用率(cpu、内存、磁盘、网络等)信息，主要用于系统性能监控
    实现了同等命令实现的功能：ps、top、lsof、netstat、ifconfig、who、df、kill、free、nice(优先级)、ionice、iotop、uptime、pidof、tty、taskset、pmap等
    跨平台：
    主要功能包含：CPU、磁盘、内存、网络、进程。
'''

'''
    psutil.cpu_count() 得到逻辑cpu的个数,logical=False时返回物理cpu
    psutil.cpu_percent() 获取cpu的平均使用率，percpu=True时返回每个cpu的使用率
'''
# import psutil
# count = psutil.cpu_count()
# percent = psutil.cpu_percent(percpu=True)
# mem_avail = psutil.virtual_memory().available
# mem_total = psutil.virtual_memory().total
# mem_used = (mem_total - mem_avail)/mem_total
# disk = psutil.disk_io_counters()
# disk_usage = psutil.disk_usage("/")
# print(disk_usage)


'''
    如何获取机器cpu的数量：cat /proc/cpuinfo |grep cores
    获取获取机器内存的使用率： free -m 中，(total-available)/total
    swap分区：一般不开启，内存空间不够用时会开启一片磁盘空间作为内存空间使用。
    系统的瓶颈一般为磁盘IO瓶颈，到iostat -x 10 中的%util达到70%为忙碌
'''

import psutil
from datetime import datetime
import time
for i in range(10):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M")
    cpu_logical_count = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    mem_total = mem.total
    mem_used_percent = (mem.total - mem.available)/mem.total
    disk = psutil.disk_usage("/")
    disk_total = disk.total
    disk_usage =  disk.percent/100
    net_io_counters = psutil.net_io_counters()
    net_in_counter = net_io_counters.bytes_recv
    net_out_counter = net_io_counters.bytes_sent
    print(time_now)
    print("cpu: 逻辑核数为", cpu_logical_count, "平均使用率为", cpu_percent)
    print("mem: 总大小为", mem_total, "使用率为", mem_used_percent)
    print("磁盘: 根目录大小为", disk_total, "使用率为", disk_usage)
    print("net: 收为", net_in_counter, "发为", net_out_counter)
    print("-----------------------------")
    time.sleep(1)