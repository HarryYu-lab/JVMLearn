"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/29 17:01
*  @Project :   JVMbyPython
*  @desc    :   未解析的属性
**************************************
"""
from ch03.classfile.AttributeInfo import AttributeInfo


class UnparsedAttribute(AttributeInfo):
    def __init__(self, attr_name, attr_len):
        self.name = attr_name
        self.length = attr_len
        self.info = ""

    def read_info(self, class_reader):
        self.info = class_reader.read_bytes(self.length)