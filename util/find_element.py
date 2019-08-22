#coding=utf-8
from util.read_init import ReadIni

# 封装具体的定位方法
# 支持id,classname,xpath定位
# 需要传入driver 进行初始化.
class FindElement:

	def __init__(self,driver):
		self.driver = driver

	def get_element(self,key):
		read_ini = ReadIni()
		local = read_ini.get_value(key)
		if local != None:
			by = local.split('>')[0]
			local_by = local.split('>')[1]
			try:
				if by == 'id':
					return self.driver.find_element_by_id(local_by)
				elif by == 'className':
					return self.driver.find_element_by_class_name(local_by)
				else:
					return self.driver.find_element_by_xpath(local_by)
			except:
				#self.driver.save_screenshot("../jpg/test02.png") # 如果获取不到具体信息,报错截图
				return None
		else:
			return None


