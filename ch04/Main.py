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
from ch04.Cmd import Cmd
from ch04.rtda import LocalVars
from ch04.rtda.Frame import Frame


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
    frame = Frame(100, 100)
    test_local_vars(frame.local_vars)
    test_operand_stack(frame.operand_stack)


# 测试局部变量表
def test_local_vars(local_vars: LocalVars):
    local_vars.set_numeric(0, 100)
    local_vars.set_numeric(1, -100)
    local_vars.set_numeric(2, 2997924580)
    local_vars.set_numeric(3, -2997924580)
    local_vars.set_numeric(4, 3.1415926)
    local_vars.set_numeric(5, 2.71828182845)
    local_vars.set_ref(6, None)
    print(local_vars.get_numeric(0))
    print(local_vars.get_numeric(1))
    print(local_vars.get_numeric(2))
    print(local_vars.get_numeric(3))
    print(local_vars.get_numeric(4))
    print(local_vars.get_numeric(5))
    print(local_vars.get_ref(6))


# 测试操作数栈
def test_operand_stack(ops):
    ops.push_numeric(100)
    ops.push_numeric(-100)
    ops.push_numeric(2997924580)
    ops.push_numeric(-2997924580)
    ops.push_numeric(3.1415926)
    ops.push_numeric(2.71828182845)
    ops.push_ref(None)
    print(ops.pop_ref())
    print(ops.pop_numeric())
    print(ops.pop_numeric())
    print(ops.pop_numeric())
    print(ops.pop_numeric())
    print(ops.pop_numeric())
    print(ops.pop_numeric())


if __name__ == '__main__':
    main()
