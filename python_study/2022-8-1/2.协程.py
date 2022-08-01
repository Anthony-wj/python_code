'''
    协程是一种用户态的轻量级线程，协程的调度完全由用户控制
    主要用于异步IO编程
'''

# def test_yield():
#     index = 0
#     while index < 99:
#         print(index)
#         yield index
#         index += 1
#
# if __name__ == '__main__':
#     itr = test_yield()
#     next(itr)
#     next(itr)

'''
    asyncio 异步编程
'''

import asyncio
async def func1():
    print(1)
    await asyncio.sleep(2) # 等同于 time.sleep(2)
    print(2)

async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)

# 创建异步编程任务列表
tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]
# 生成事件循环
loop = asyncio.get_event_loop()

# 运行
loop.run_until_complete(asyncio.wait(tasks))

