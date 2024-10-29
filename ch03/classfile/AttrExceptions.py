"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/29 16:53
*  @Project :   JVMbyPython
*  @desc    :   记录方法抛出的异常表
**************************************
"""

from ch03.classfile.AttributeInfo import AttributeInfo


class ExceptionsAttribute(AttributeInfo):
    def __init__(self):
        self.exception_index_table = []

    def read_info(self, class_reader):
        self.exception_index_table = class_reader.read_unit16s()