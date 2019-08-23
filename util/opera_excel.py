# coding=utf-8
import xlrd
import os
from xlutils.copy import copy

path = os.path.abspath(os.path.dirname(os.getcwd()) + '/config/case.xls')

#
# excel 文件操作类
# xlwd 只能操作.xls Excel 文件
# 另一个框架"openpyxl",对'.xls','.xlsx' 都能操作
#
class OperaExcel:

    def __init__(self, file_path=None, i=None):
        if file_path == None:
            self.file_path = path
        else:
            self.file_path = file_path
        if i == None:
            i = 0
        self.excel = self.get_excel()
        self.data = self.get_sheets(i)

    def get_excel(self):
        '''
        获取excel
        '''
        excel = xlrd.open_workbook(self.file_path)
        return excel

    def get_sheets(self, i):
        '''
        获取sheets的内容
        '''
        tables = self.excel.sheets()[i]
        return tables

    def get_lines(self):
        '''
        获取excel行数
        '''
        lines = self.data.nrows
        return lines

    def get_cell(self, row, cell):
        """
        获取目标单元格内容
        :param row:  目标行
        :param cell: 目标列
        :return: 返回目标单元格内容
        """
        data = self.data.cell(row, cell).value
        return data

    def write_value(self, row, value):
        read_value = self.excel
        write_data = copy(read_value)
        write_save = write_data.get_sheet(0)
        write_save.write(row, 8, value)
        write_data.save(self.file_path)


if __name__ == '__main__':
    opera = OperaExcel()
    print(opera.get_lines())
    # print(opera.write_value(6, 'pass'))
