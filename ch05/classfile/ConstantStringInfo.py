"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/28 17:20
*  @Project :   JVMbyPython
*  @desc    :   表示java.lang.String字面量
**************************************
"""

from ch05.classfile.ConstantInfo import ConstantInfo


class ConstantStringInfo(ConstantInfo):
    def __init__(self, constant_pool):
        from ch05.classfile.ConstantPool import ConstantPool
        self.cp = ConstantPool(constant_pool)
        self.string_index = ""

    # 读取常量池索引
    def read_info(self, class_reader):
        self.string_index = int.from_bytes(class_reader.read_unit16(), byteorder="big")

    def __str__(self):
        return self.cp.get_utf8(self.string_index)
