# coding=utf-8

from run.get_data import GetData
from run.action_method import ActionMethod
from util.server import Server

#
# 关键字模式运行类
# 调用了python getattr(对象类,'函数名')函数,返回具体目标函数.
#
class RunMain:

    def run_method(self):
        server = Server()
        server.main()  # 多线程启动服务
        data = GetData()  # 关键字文件封装类
        action_method = ActionMethod() #
        lines = data.get_case_lines()# 获取excel中具体 case 数量

        #从第2行开始取:
        for i in range(1, lines):
            handle_step = data.get_handle_step(i)
            element_key = data.get_element_key(i)
            handle_value = data.get_handle_value(i)
            expect_key = data.get_expect_element(i)
            expect_step = data.get_expect_handle(i)#预期步骤,对应为:get_element()方法

            execute_method = getattr(action_method, handle_step)
            if element_key != None:
                execute_method(element_key, handle_value)
            else:
                execute_method(handle_value)
            if expect_step != None:
                expect_result = getattr(action_method, expect_step)# 获取.ini文件操作
                result = expect_result(expect_key)#获取.init 具体值
                if result:#判断是否存在具体元素值
                    data.write_value(i, "pass")
                else:
                    data.write_value(i, "fail")


if __name__ == '__main__':
    run = RunMain()
    run.run_method()
