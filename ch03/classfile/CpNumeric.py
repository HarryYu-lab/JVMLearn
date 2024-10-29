"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/28 16:25
*  @Project :   JVMbyPython
*  @desc    :   用一个module编写数值常量类
**************************************
"""
import ctypes
import struct

from ch03.classfile.ConstantInfo import ConstantInfo

# 使用4字节存储整数常量
class ConstantIntegerInfo(ConstantInfo):
    def __init__(self):
        self.val = 0

    # 先读取一个uint32数据，然后把它转型成int32类型
    def read_info(self, class_reader):
       bytes_data = int.from_bytes(class_reader.read_unit32(), byteorder='big')
       self.val = ctypes.c_int32(bytes_data).value


class ConstantFloatInfo(ConstantInfo):
    def __init__(self):
        self.val = 0.0

    # 先读取一个uint32数据，然后把它转型成int32类型
    def read_info(self, class_reader):
        bytes_data = int.from_bytes(class_reader.read_uint32(), byteorder='big')
        self.val = struct.unpack('>f', struct.pack('>l', bytes_data))[0]

    # 使用8字节存储整数常量
class ConstantLongInfo(ConstantInfo):
    def __init__(self):
        self.val = 0

    # 先读取一个uint64数据，然后把它转型成int64类型
    def read_info(self, class_reader):
        bytes_data = int.from_bytes(class_reader.read_unit64(), byteorder='big')
        self.val = ctypes.c_int64(bytes_data).value

# 使用8字节存储IEEE754双精度浮点数
class ConstantDoubleInfo(ConstantInfo):
    def __init__(self):
        self.val = 0.0

    def read_info(self, class_reader):
        bytes_data = int.from_bytes(class_reader.read_unit64(), byteorder='big')
        self.val = struct.unpack('>d', struct.pack('>q', bytes_data))[0]