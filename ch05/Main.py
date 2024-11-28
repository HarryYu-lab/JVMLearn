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
from ch05.Cmd import Cmd
from ch05.Interpreter import Interpreter
from ch05.classfile.ClassFile import ClassFile
from ch05.classpath import Classpath


def main(input_args=None):
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
    # 打印命令行参数
    print("classpath:{0} class:{1} args:{2}".format(class_path, cmd.class_name, cmd.args))

    class_name = cmd.class_name.replace(".", "/")
    # 读取并解析class文件
    cf = load_class(class_name, class_path)
    # 查找类的main()方法
    main_method = get_main_method(cf)
    if main_method:
        # 调用interpret()函数解释执行main()方法
        Interpreter.interpret(main_method)
    else:
        print("Main method not found in class {0}".format(cmd.class_name))


# 读取并解析class文件
def load_class(class_name, class_path: Classpath):
    class_data, _, error = class_path.read_class(class_name)

    class_file = ClassFile()
    cf = class_file.parse(class_data)
    return cf


# 查找类的main()方法
def get_main_method(classFile):
    for m in classFile.methods:
        if m.name == "main" and m.descriptor == "([Ljava/lang/String;)V":
            return m
    return None


if __name__ == '__main__':
    Xjre_path = os.path.join(os.environ.get("JAVA_HOME"), "jre")
    # 得到项目路径的绝对地址
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    # 得到java的用户类路径
    resources_path = os.path.join(os.path.dirname(root_path), "JVMbyPython/java/class")

    # 采用指定用户类路径--cp，执行GaussTest程序
    fake_args = ['--Xjre', Xjre_path, '--cp', resources_path, 'ch05.GaussTest']
    main(fake_args)

    # 采用指定用户类路径--cp，执行ShTest程序
    # fake_args = ['--Xjre', Xjre_path, '--cp', resources_path, 'jvmgo.book.ch05.ShTest']
    # main(fake_args)
