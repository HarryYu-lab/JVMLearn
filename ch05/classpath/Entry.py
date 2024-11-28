"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/9 16:07
*  @Project :   JVMbyPython
*  @desc    :   类路径的基类
**************************************
"""
from abc import ABCMeta, abstractmethod
class Entry(metaclass=ABCMeta):
    # 路径分隔符
    path_list_separator = ";"

    # 寻找和加载class文件，接口方法
    @abstractmethod
    def read_class(self, class_name):
        pass

    # 根据参数常见不同类型的Entry实例
    @staticmethod
    def new_entry(path):
        from ch05.classpath.CompositeEntry import CompositeEntry
        from ch05.classpath.ZipEntry import ZipEntry
        from ch05.classpath.DirEntry import DirEntry
        from ch05.classpath.WildcardEntry import WildcardEntry

        if Entry.path_list_separator in path:
            return CompositeEntry(path)
        elif path.endswith("*"):
            return WildcardEntry(path)
        elif path.endswith(".jar") or path.endswith(".JAR") or path.endswith(".zip") or path.endswith(".ZIP"):
            return ZipEntry(path)
        else:
            return DirEntry(path)



