'''
    协程是一种用户态的轻量级线程，协程的调度完全由用户控制
'''

def test_yield():
    index = 0
    while index < 99:
        print(index)
        yield index
        index += 1

if __name__ == '__main__':
    itr = test_yield()
    next(itr)
    next(itr)
