"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/9 16:14
*  @Project :   JVMbyPython
*  @desc    :   Zip或JAR文件形式的类路径（继承Entry类）
**************************************
"""

from ch02.classpath.Entry import Entry
import os.path
import zipfile


class ZipEntry(Entry):
    