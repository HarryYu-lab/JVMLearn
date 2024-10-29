"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/9 11:40
*  @Project :   JVMbyPython
*  @desc    :   main函数
**************************************
"""

import os
import argparse
from ch03.Cmd import Cmd
from ch03.classfile.ClassFile import ClassFile
from ch03.classpath import Classpath


def main(input_args):
    parser = argparse.ArgumentParser(description="Usage of argparse")

    parser.add_argument("-v", "--version", action="store_true", default=False, dest="version_flag",
                        help="print version and exit.")
    parser.add_argument("--cp", action="store", type=str, dest="cpOption", help="classpath")
    parser.add_argument("--claspath", action="store", type=str, dest="cpOption", help="classpath")
    parser.add_argument('--Xjre', action="store", type=str, dest="XjreOption", help="path to jre")
    parser.add_argument('args', nargs='*', help='additional arguments')

    options = parser.parse_args(input_args)

    if options:
        cmd = Cmd(options, options.args)

        if not options.version_flag:
            start_JVM(cmd)


# 启动JVM函数
def start_JVM(cmd):
    # 解析类路径

    class_path = Classpath.Classpath.parse(cmd.XjreOption, cmd.cpOption)

    # 读取主类数据
    class_name = cmd.class_name.replace(".", "/")

    class_file = load_class(class_name, class_path)
    print(cmd.class_name)
    print_class_info(class_file)


# 加载class
def load_class(class_name, class_path):
    class_data, _, error = class_path.read_class(class_name)

    class_file = ClassFile()
    cf = class_file.parse(class_data)
    return cf


# 把class文件的一些重要信息打印出来
def print_class_info(class_file):
    print("version: {0}.{1}".format(class_file.major_version, class_file.minor_version))
    print("constants count: {0}".format(len(class_file.constant_pool.cp)))
    print("access flags: {0}".format(hex(int.from_bytes(class_file.access_flags, byteorder="big"))))
    print("this class: {0}".format(class_file.class_name))
    print("super class: {0}".format(class_file.super_class_name))
    print("interfaces: {0}".format(class_file.interface_names))
    print("fields count: {0}".format(len(class_file.fields)))
    for f in class_file.fields:
        print("   {0}".format(f.name))
    print("methods count: {0}".format(len(class_file.methods)))
    for m in class_file.methods:
        print("   {0}".format(m.name))


if __name__ == '__main__':
    Xjre_path = os.path.join(os.environ.get("JAVA_HOME"), "jre")

    # 指定-Xjre选项和类名
    fake_args = ['--Xjre', Xjre_path, 'java.lang.String']
    # fake_args = ['--Xjre', Xjre_path, 'java/lang/CharSequence']
    main(fake_args)
