"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/28 15:14
*  @Project :   JVMbyPython
*  @desc    :   属性表类
**************************************
"""
from abc import ABCMeta, abstractmethod


class AttributeInfo(metaclass=ABCMeta):

    @abstractmethod
    def read_info(self, class_reader):
        pass

    # 读取属性表
    @staticmethod
    def read_attributes(class_reader, constant_pool):
        attributes_count = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        attributes = []
        for i in range(attributes_count):
            attributes.append(AttributeInfo.read_attribute(class_reader, constant_pool))
        return attributes

    # 读取单个属性
    @staticmethod
    def read_attribute(class_reader, constant_pool):
        attr_name_index = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        attr_name = ""
        if attr_name_index != 0:
            attr_name = constant_pool.get_utf8(attr_name_index)
        attr_len = int.from_bytes(class_reader.read_unit32(), byteorder="big")
        attr_info = AttributeInfo.new_attribute_info(attr_name, attr_len, constant_pool)
        attr_info.read_info(class_reader)
        return attr_info

    @staticmethod
    def new_attribute_info(attr_name, attr_len, constant_pool):
        from .AttrCode import CodeAttribute
        from .AttrConstantValue import ConstantValueAttribute
        from .AttrMarkers import DeprecatedAttribute, SyntheticAttribute
        from .AttrExceptions import ExceptionsAttribute
        from .AttrLineNumberTable import LineNumberTableAttribute
        from .AttrSourceFile import SourceFileAttribute
        from .AttrUnparsed import UnparsedAttribute
        from .AttrLocalVariableTable import LocalVariableTableAttribute

        if attr_name == "Code":
            return CodeAttribute(constant_pool)
        elif attr_name == "ConstantValue":
            return ConstantValueAttribute()
        elif attr_name == "Deprecated":
            return DeprecatedAttribute()
        elif attr_name == "Exceptions":
            return ExceptionsAttribute()
        elif attr_name == "LineNumberTable":
            return LineNumberTableAttribute()
        elif attr_name == "LocalVariableTable":
            return LocalVariableTableAttribute()
        elif attr_name == "SourceFile":
            return SourceFileAttribute(constant_pool)
        elif attr_name == "Synthetic":
            return SyntheticAttribute()
        else:
            return UnparsedAttribute(attr_name, attr_len)
