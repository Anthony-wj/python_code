# with open("text.txt", "w",) as f:
#     f.write("xixihaha")

'''
    上下文管理器：作为确保资源正确清理的一种方式
    用__enter__和__exit__方法
    with语句先执行__enter__方法，然后执行内容，退出的时候自动执行__exit__方法
    with语句结束都是执行__exit__函数
        正常退出的话，__exit__接收三个参数都是None
        异常退出时：三个参数为sys.exc_info()函数的三个值：类型(异常类)、值(异常实例)、跟踪记录
    上下文管理器的作用：完成分配和释放资源


'''

# fp = open("text.txt", "a+")
# fp.__enter__() # 打开文件
# fp.__exit__() # 关闭文件
#
# class Value_Error(ValueError):
#     def __str__(self):
#         return "I am ValueError"
#
# class ContextManager():
#     def __enter__(self):
#         print("This is enter")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("This is exit")
#         if issubclass(exc_type, ValueError):
#             return True
#         return False
# with ContextManager() as c:
#     raise Value_Error
#     raise ValueError
#     print("This is with syntax")

import contextlib

@contextlib.contextmanager
def mycontext():
    print("enter context")
    yield
    print("exit context")

with mycontext():
    print("xxxxxxxxxxxxxxxx")


class ShellException():
    def __str__(self):
        return "404执行失败"

