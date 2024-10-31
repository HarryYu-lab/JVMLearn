"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/29 10:32
*  @Project :   JVMbyPython
*  @desc    :   表示类或者接口的符号引用
**************************************
"""

from ch04.classfile.ConstantInfo import ConstantInfo


class ConstantClassInfo(ConstantInfo):
    def __init__(self, constant_pool):
        from ch04.classfile.ConstantPool import ConstantPool
        self.cp = ConstantPool(constant_pool)
        self.name_index = 0

    def read_info(self, class_reader):
        self.name_index = int.from_bytes(class_reader.read_unit16(), byteorder="big")

    @property
    def name(self):
        return self.cp.get_utf8(self.name_index)
