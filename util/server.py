# coding=utf-8
from util.dos_cmd import DosCmd
from util.port import Port
import threading
import time
from util.write_user_command import WriteUserCommand


# 无 GUI 启动 Appium 服务
# 封装了操作 appium 服务等一些命令行方法.
class Server:

    # 初始化
    def __init__(self):
        self.dos = DosCmd()  # Dos 命令行操作类
        self.device_list = self.get_devices()  # 调用本类内部函数get_devices() 获取设备信息
        self.write_file = WriteUserCommand()  # yaml文件操作类

    def get_devices(self):
        '''
        获取设备信息
        打印2: ['List of devices attached ', '192.168.226.101:5555\tdevice']
        打印3: ['List of devices attached \n', '192.168.226.101:5555\tdevice\n', '\n']
        获取到的结果应该从第二位获取
        如果没有设备连接则返回数组:['List of devices attached ']
        '''
        devices_list = []
        result_list = self.dos.excute_cmd_result('adb devices')
        if len(result_list) >= 2:
            for i in result_list:
                if 'List' in i:
                    # 如果是'List of devices attached' 则跳过,不打印
                    continue
                devices_info = i.split('\t')  # 分割后只获取IP+端口号.
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            return None

    def create_port_list(self, start_port):
        """
        创建可用端口 port
        内部检查 port 端口是否被占用,返回device_list一样数量的端口号
        :param start_port: 端口号
        :return: 返回可用的端口数组.
        """
        port = Port()  # 端口工具类
        port_list = []
        port_list = port.create_port_list(start_port, self.device_list)  # 调用Dos工具类,device_list 参数为设备号:IP+端口
        return port_list

    def create_command_list(self, i):
        """
        生成启动服务命令
        # appium -p 4723 -bp 4726 -U 127.0.0.1:62001 --no-reset --session-override --log E:/Teacher/Imooc/AppiumPython/log/test01.log
        # appium -p 4700 -bp 4701 -U 127.0.0.1:21503
        """
        command_list = []
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4900)
        device_list = self.device_list
        command = "appium -p " + str(appium_port_list[i]) + " -bp " + str(bootstrap_port_list[i]) + " -U " + \
                  device_list[i] + " --no-reset --session-override --log E:/Teacher/Imooc/AppiumPython/log/test02.log"
        command_list.append(command)
        # 经检查没有被占用的端口号,与之对应的设备devices启动命令
        self.write_file.write_data(i, device_list[i], str(bootstrap_port_list[i]), str(appium_port_list[i]))
        return command_list

    def start_server(self, i):
        '''
        启动服务
        可以通过多线程,根据设备数启动服务
        '''
        self.start_list = self.create_command_list(i) #生成命令
        print(self.start_list)
        self.dos.excute_cmd(self.start_list[0])#执行命令

    def kill_server(self):
        server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list) > 0:
            self.dos.excute_cmd('taskkill -F -PID node.exe')

    def main(self):
        """
        这里使用threading 框架启动,
        :return:
        """
        thread_list = []
        self.kill_server()
        self.write_file.clear_data()
        for i in range(len(self.device_list)):
            appium_start = threading.Thread(target=self.start_server, args=(i,))
            thread_list.append(appium_start)
        for j in thread_list:
            j.start()
        time.sleep(25)


if __name__ == '__main__':
    server = Server()
    # print(server.main())
    print('打印:', server.get_devices())
    print('打印2:', server.dos.excute_cmd_result('adb devices'))
