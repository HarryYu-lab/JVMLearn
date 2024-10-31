"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/28 15:11
*  @Project :   JVMbyPython
*  @desc    :   class文件的结构
**************************************
"""
from ch04.classfile.AttributeInfo import AttributeInfo
from ch04.classfile.ClassReader import ClassReader
from ch04.classfile.ConstantPool import ConstantPool
from ch04.classfile.MemberInfo import MemberInfo

class ClassFile:
    def __init__(self):
        # 魔数
        self.magic = ""
        # 小版本号
        self.minor_version = ""
        # 主版本号
        self.major_version = ""
        # 常量池
        self.constant_pool = None
        # 类访问标志，用于指出class文件定义的是类还是接口，访问级别是public还是private
        self.access_flags = ""
        # 类索引
        self.this_class = ""
        # 超类索引
        self.super_class = ""
        # 接口索引表
        self.interfaces = []
        # 变量
        self.fields = []
        # 方法
        self.methods = []
        # 属性
        self.attributes = []

    def parse(self, class_data):
        class_reader = ClassReader(class_data)
        self.read(class_reader)
        return self

    def read(self, class_reader):
        self.read_and_check_magic(class_reader)
        self.read_and_check_version(class_reader)

        self.constant_pool = ConstantPool()
        self.constant_pool.read_constant_pool(class_reader)

        self.access_flags = class_reader.read_unit16()
        self.this_class = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        self.super_class = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        self.interfaces = class_reader.read_unit16s()

        memberInfo = MemberInfo(self.constant_pool)
        self.fields = memberInfo.read_members(class_reader, self.constant_pool)
        self.methods = memberInfo.read_members(class_reader, self.constant_pool)
        self.attributes = AttributeInfo.read_attributes(class_reader, self.constant_pool)

    # 读取并检查Class文件的起始字节，必须以0xCAFEBABE固定字节开头
    @staticmethod
    def read_and_check_magic(class_reader):
        magic = class_reader.read_unit32()
        if magic != b'\xca\xfe\xba\xbe':
            raise RuntimeError("java.lang.ClassFormatError: magic!")

    # 读取并检查版本号，由于采用java1.8的编译器，故支持版本号为45.0~52.0的class文件
    def read_and_check_version(self, class_reader):
        self.minor_version = int.from_bytes(class_reader.read_unit16(), byteorder='big')
        self.major_version = int.from_bytes(class_reader.read_unit16(), byteorder='big')

        if self.major_version == 45:
            return
        elif self.major_version in {46, 47, 48, 49, 50, 51, 52}:
            if self.minor_version == 0:
                return
        raise RuntimeError("java.lang.UnsupportedClassVersionError!")

    # 从常量池中查找类名
    @property
    def class_name(self):
        return self.constant_pool.get_class_name(self.this_class)

    # 从常量池中查找超类类名
    @property
    def super_class_name(self):
        if self.super_class:
            return self.constant_pool.get_class_name(self.super_class)
        # 只有java.lang.Object没有超类
        return ""

    # 从常量池中查找接口名
    @property
    def interface_names(self):
        return [self.constant_pool.get_class_name(cpName) for cpName in self.interfaces]