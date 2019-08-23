# coding=utf-8
import time
from appium import webdriver
from util.write_user_command import WriteUserCommand
import os

apk_path = os.path.abspath(os.path.dirname(os.getcwd()) + 'mukewang.apk')


class BaseDriver:

    # 通过线程启动
    # devices_name adb devices
    # port
    def android_driver(self, i):
        print("this is android_driver:", i)
        write_file = WriteUserCommand()
        devices = write_file.get_value('user_info_' + str(i), 'deviceName')
        port = write_file.get_value('user_info_' + str(i), 'port')
        # "automationName":"UiAutomator2",
        # "newCommandTimeout":'180'
        capabilities = {
            "platformName": "Android",
            "deviceName": devices,
            "app": apk_path,
            "appWaitActivity": "cn.com.open.mooc.user.login.MCLoginActivity",
            "noReset": "true",
            "platforVersion": "7.0.0",
            "appPackage": "cn.com.open.mooc"
        }
        driver = webdriver.Remote("http://127.0.0.1:" + port + "/wd/hub", capabilities)
        time.sleep(10)
        return driver
