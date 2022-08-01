import sys
print(sys.modules)
print(sys.path)
# sys.path是存放寻找模块的路径，用列表存储，使用较多


'''
    如何讲外部参数如何传入python程序
    [root@Seesunman 2022-8-1]# cat log_import.py 
    import sys
    print("start")
    print(sys.argv)
    [root@Seesunman 2022-8-1]# python3 log_import.py 1 2
    start
    ['log_import.py', '1', '2']
'''

'''
    argparse使用方法：
    1.创建ArgumentParser()对象
    2.调用add_argument()方法添加参数
    3.使用parse_args()解析参数

    import argparse 
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", dest="na", help="input file name")
    parser.add_argument("-t", "--log-time", dest="lt", help="input log time")
    args = parser.parse_args()
    print(args)
'''

