import unittest
import mod1

class TestFunc(unittest.TestCase):
    # 函数名以test开头
    def setUp(self): # 测试用例执行之前都会执行setUp
        print("start......")
    def tearDown(self): # 测试用例执行之后会执行tearDown
        print("end......")
    def test_add(self):
        print("test_add......")
        self.assertEqual(3, mod1.add(1, 2))
    def test_xxx(self):
        print("test_add2......")
        self.assertEqual(3, mod1.add(1, 2))

if __name__ == "__main__":
    # unittest.main() # 会自动执行以test开头的测试用例
    # main继承了四个模块功能，包含整个过程
    suit = unittest.TestSuite() # 创建一个容器
    suit.addTest(TestFunc("test_add")) # 添加要执行的测试用例
    runner = unittest.TextTestRunner() # 执行测试用例的运行对象
    runner.run(suit) # 运行测试用例
'''
unittest包含4个模块
    TestCase
    TestSuite
    TextTestRuner
    TestLoader
'''