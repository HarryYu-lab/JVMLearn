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
from ch02.Cmd import Cmd
from ch02.classpath import Classpath


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


def start_JVM(cmd):
    # 解析类路径

    class_path = Classpath.Classpath.parse(cmd.XjreOption, cmd.cpOption)
    # 打印命令行参数
    print("classpath: {0} class: {1} args: {2}".format(class_path, cmd.class_name, cmd.args))

    # 读取主类数据
    class_name = cmd.class_name.replace(".", "/")

    class_data, _, error = class_path.read_class(class_name)
    if error:
        print("Could not find or load main class {0}\n".format(cmd.class_name))
        exit(0)

    # 打印class里面的数据信息
    print("class data: {0}".format([int(hex(d), 16) for d in class_data]))


if __name__ == '__main__':
    Xjre_path = os.path.join(os.environ.get("JAVA_HOME"), "jre")

    # 指定-Xjre选项和类名
    fake_args = ['--Xjre', Xjre_path, 'java.lang.Object']
    main(fake_args)
