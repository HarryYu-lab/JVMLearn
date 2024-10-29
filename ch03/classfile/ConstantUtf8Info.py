"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/28 17:12
*  @Project :   JVMbyPython
*  @desc    :   MUTF-9编码的字符串类
**************************************
"""

from ch03.classfile.ConstantInfo import ConstantInfo
import ctypes


class ConstantUtf8Info(ConstantInfo):
    def __init__(self):
        self.str = ""

    # 先读取出byte[]，然后调用decode_mutf8()函数把它解码成字符串
    def read_info(self, class_reader):
        length = ctypes.c_uint32(int.from_bytes(class_reader.read_unit16(), byteorder='big')).value
        if length == 0:
            self.str = ""
        else:
            bytes = class_reader.read_bytes(length)
            self.str = self.decode_mutf8(bytes)

    @staticmethod
    def decode_mutf8(bytes_data):
        return bytes_data.decode()
