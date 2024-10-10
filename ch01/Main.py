"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/9 11:40
*  @Project :   JVMbyPython
*  @desc    :   main函数
**************************************
"""

import argparse
from ch01.Cmd import Cmd


def main(input_args):
    parser = argparse.ArgumentParser(description='Usage of argparse')
    parser.add_argument("-v", "--version", action="store_true", default=False, dest="version_flag",
                        help="print version and exit.")
    parser.add_argument("--cp", action="store", type=str, dest="cpOption", help="classpath")
    parser.add_argument("--claspath", action="store", type=str, dest="cpOption", help="classpath")
    parser.add_argument('args', nargs='*', help='additional arguments')

    options = parser.parse_args(input_args)

    if options:
        cmd = Cmd(options, options.args)

        if not options.version_flag:
            start_JVM(cmd)


def start_JVM(cmd):
    cmd.print_classpath()


if __name__ == '__main__':
    fake_argvs = ['-v']
    main(fake_argvs)

    fake_argvs = ['--cp', 'foo/bar', 'MyApp', 'arg1', 'arg2']
    main(fake_argvs)
