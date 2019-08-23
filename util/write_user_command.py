# coding=utf-8
import yaml
import os
import json

path = os.path.abspath(os.path.dirname(os.getcwd()) + '/config/userconfig.yaml')


# 存储用户命令
class WriteUserCommand:

    def read_data(self):
        '''
        加载yaml数据
        '''
        with open(path, 'r') as fr:
            data = yaml.load(stream=fr, Loader=yaml.FullLoader)
        return data

    def get_value(self, key, port):
        '''
        获取value
        '''
        data = self.read_data()
        value = data[key][port]
        return value

    def write_data(self, i, device, bp, port):
        '''
        写入数据
        '''
        data = self.join_data(i, device, bp, port)
        with open(path, "a") as fr:
            yaml.dump(data, fr)

    # 写入格式
    def join_data(self, i, device, bp, port):
        data = {
            "user_info_" + str(i): {
                "deviceName": device,
                "bp": bp,
                "port": port
            }
        }
        return data

    def clear_data(self):
        with open(path, "w") as fr:
            fr.truncate()
        fr.close()

    def get_file_lines(self):
        data = self.read_data()
        return len(data)


if __name__ == '__main__':
    write_file = WriteUserCommand()
    data = write_file.get_value('user_info_0', 'bp')
    print(data)
