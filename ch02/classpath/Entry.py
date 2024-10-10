"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/9 16:07
*  @Project :   JVMbyPython
*  @desc    :   类路径的基类
**************************************
"""
from abc import ABCMeta, abstractmethod
class Entry(ABCMeta):
    # 路径分隔符
    path_list_separator = ";"

    # 寻找和加载class文件，接口方法
    @abstractmethod
    def red_class(self, class_name):
        pass

    @staticmethod
    def new_entry(path):


