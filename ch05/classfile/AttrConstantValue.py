"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/29 16:46
*  @Project :   JVMbyPython
*  @desc    :   用于表示常量表达式的值
**************************************
"""
from ch05.classfile.AttributeInfo import AttributeInfo


class ConstantValueAttribute(AttributeInfo):
    def __init__(self):
        self.constant_value_index = 0

    def read_info(self, class_reader):
        self.constant_value_index = int.from_bytes(class_reader.read_unit16(), byteorder='big')
