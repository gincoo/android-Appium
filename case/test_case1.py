# coding=utf-8
import sys

# sys.path.append("E:/Teacher/Imooc/AppiumPython")
import unittest
import HTMLTestRunner
import multiprocessing
import time
import os
from util.server import Server
from business.login_business import LoginBusiness
from util.write_user_command import WriteUserCommand

dir_path = os.path.dirname(os.getcwd())

#
# UnitTest 执行
#
class ParameTestCase(unittest.TestCase):

    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames #设置全局变量
        parames = parame


class CaseTest(ParameTestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpclass---->", parames)
        cls.login_business = LoginBusiness(parames)

    def setUp(self):
        print("this is setup\n")

    def test_01(self):
        print("test case 里面的参数", parames)
        self.login_business.login_pass()

    @unittest.skip("CaseTest")
    def test_02(self):
        self.login_business.login_user_error()
        print("this is case02\n")
        # self.assertNotEqual(1,2)
        # self.assertTrue(flag)
        # self.assertFalse(flag)
        self.assertTrue(True)

    def tearDown(self):
        time.sleep(1)
        print("this is teardown\n")
        # 判断是否存在异常信息,如果存在则截图
        if sys.exc_info()[0]:
            self.login_business.login_handle.login_page.driver.save_screenshot("../jpg/test02.png")

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print("this is class teardown\n")


# cls.driver.quit()


def appium_init():
    server = Server()
    server.main()


def get_suite(i):
    print("get_suite里面的", i)
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_02", parame=i))
    suite.addTest(CaseTest("test_01", parame=i))
    # 使用unitest执行:unittest.TextTestRunner().run(suite)
    # 使用HTMLTestRunner 报告执行生成
    html_file = os.path.abspath(dir_path + '/report/' + str(i) + ".html")
    fp = open(html_file, "wb")
    HTMLTestRunner.HTMLTestRunner(stream=fp).run(suite)


def get_count():
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count


if __name__ == '__main__':
    appium_init()
    # get_suite(0)
    threads = []
    for i in range(get_count()):
        print(i)
        t = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()

# time.sleep(1)
# time.sleep(80)
