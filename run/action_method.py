# coding=utf-8
from util.find_element import FindElement
from base.base_driver import BaseDriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#
# 封装了具体的 appium API 操作控制
#
class ActionMethod:

    def __init__(self):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(0)
        self.find_element = FindElement(self.driver)

    def input(self, *args):
        """
        输入值
        """
        # key,value
        element = self.find_element.get_element(args[0])
        if element == None:
            return args[0], "元素没找到"
        element.send_keys(args[1])

    def on_click(self, *args):
        '''
        元素点击
        '''
        element = self.find_element.get_element(args[0])
        if element == None:
            return args[0], "元素没找到"
        element.click()

    def sleep_time(self, *args):
        time.sleep(int(args[0]))

    # 获取屏幕的宽高
    def get_size(self, *args):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左边滑动
    def swipe_left(self, *args):
        # [100,200]
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1, 2000)

    # 向右边滑动
    def swipe_right(self, *args):
        # [100,200]
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x, y1, 2000)

    # 向上滑动
    def swipe_up(self, *args):
        # [100,200]direction
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 6
        y = self.get_size()[1] / 10 * 2
        self.driver.swipe(x1, y1, x1, y, 1000)

    # 向下滑动
    def swipe_down(self, *args):
        # [100,200]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y)

    def get_element(self, *args):
        element = self.find_element.get_element(args[0])
        if element == None:
            return None
        return element

    def get_toast_element(self, *args):
        '''
        使用 WebDriverWait等待,判断是否存在 toast_element 具体目标元素
        '''
        # time.sleep(2)
        toast_element = ("xpath", "//*[contains(@text," + args[0] + ")]")
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_element))
