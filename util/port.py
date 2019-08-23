#coding=utf-8
from util.dos_cmd import DosCmd

# 端口操作工具类
class Port:

	def port_is_used(self,port_num):
		"""
		判断端口是否被占用
		:param port_num: 需要检查的端口号
		:return: 如果占用返回True ,没有占用返回False
		"""
		flag = None
		self.dos = DosCmd()
		command = 'netstat -ano | findstr '+str(port_num)
		result = self.dos.excute_cmd_result(command)
		if len(result)>0:
			flag = True
		else:
			flag = False
		return flag

	def create_port_list(self,start_port,device_list):
		"""
		start_port 4701
		生成可用端口
		:param start_port:
		:param device_list:
		:return: 如果成功
		"""
		port_list = []
		if device_list != None:
			while len(port_list) != len(device_list):
				if self.port_is_used(start_port) != True:
					# 如果没有被占用
					port_list.append(start_port)
				start_port = start_port +1
			return port_list
		else:
			print("生成可用端口失败")
			return None




if __name__ == '__main__':
	port = Port()
	li = [1,2,3,4,5]
	print(port.create_port_list(999,li))