#coding=utf-8
import os

# 命令行输入工具类
class DosCmd:

	def excute_cmd_result(self,command):
		"""
		传入具体命令,返回结果
		:param command: 具体命令
		:return: 返回结果
		"""
		result_list = []
		result = os.popen(command).readlines()#获取所有的返回值
		for i in result:
			if i =='\n':# 避免重复,readlines()已保留了换行符,
				continue

			result_list.append(i.strip('\n'))
		return result_list

	def excute_cmd(self,command):
		os.system(command)

if __name__ == '__main__':
	print('helloworld')
	# dos = DosCmd()
	# print(dos.excute_cmd_result('adb devices'))