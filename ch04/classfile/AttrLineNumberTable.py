"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/29 16:56
*  @Project :   JVMbyPython
*  @desc    :   LineNumberTable属性表存放方法的行号信息
**************************************
"""
from ch04.classfile.AttributeInfo import AttributeInfo


class LineNumberTableAttribute(AttributeInfo):
    def __init__(self):
        self.lineNumberTable = []

    def read_info(self, class_reader):
        line_number_table_length = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        self.lineNumberTable = []
        for i in range(line_number_table_length):
            line_number_table_entry = LineNumberTableEntry()
            line_number_table_entry.start_pc = int.from_bytes(class_reader.read_unit16(), byteorder="big")
            line_number_table_entry.line_number = int.from_bytes(class_reader.read_unit16(), byteorder="big")
            self.lineNumberTable.append(line_number_table_entry)


class LineNumberTableEntry():
    def __init__(self):
        self.start_pc = 0
        self.line_number = 0