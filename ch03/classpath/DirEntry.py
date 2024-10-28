"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/9 16:14
*  @Project :   JVMbyPython
*  @desc    :   目录形式的类路径（继承Entry类）
**************************************
"""

from ch03.classpath.Entry import Entry
import os


class DirEntry(Entry):

    def __init__(self, path):
        self.absDir = os.path.abspath(path)

    def read_class(self, class_name):
        file_name = os.path.join(self.absDir, class_name)
        data, error = None, None
        try:
            data = open(file_name, "rb").read()
        except IOError as e:
            error = e

        return data, self, error

    # 当打印对象的时候调用这个方法
    def __str__(self):
        return self.absDir
