"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/29 16:40
*  @Project :   JVMbyPython
*  @desc    :   SourceFile属性，用于指出源文件名。
**************************************
"""

from ch05.classfile.AttributeInfo import AttributeInfo


class SourceFileAttribute(AttributeInfo):
    def __init__(self, constant_pool):
        self.cp = constant_pool
        self.sourceFile_index = 0

    def read_info(self, class_reader):
        self.sourceFile_index = int.from_bytes(class_reader.read_unit16(), byteorder='big')

    @property
    def file_name(self):
        return self.cp.get_utf8(self.sourceFile_index)