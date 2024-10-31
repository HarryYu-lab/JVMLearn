"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/29 10:45
*  @Project :   JVMbyPython
*  @desc    :   表示字段或方法的名称和描述符
**************************************
"""

from ch04.classfile.ConstantInfo import ConstantInfo


class ConstantNameAndTypeInfo(ConstantInfo):

    def __init__(self):
        self.name_index = 0
        self.description_index = 0

    def read_info(self, class_reader):
        self.name_index = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        self.description_index = int.from_bytes(class_reader.read_unit16(), byteorder="big")