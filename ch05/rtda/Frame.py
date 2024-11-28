"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/31 15:09
*  @Project :   JVMbyPython
*  @desc    :   帧
**************************************
"""
from ch05.rtda import Thread
from ch05.rtda.LocalVars import LocalVars
from ch05.rtda.OperandStack import OperandStack


class Frame:
    def __init__(self, thread:Thread, max_locals, max_stack):
        # 用来实现链表数据结构
        self.lower = None
        self.thread = thread
        # 保存局部变量表指针
        self.local_vars = LocalVars(max_locals)
        # 保存操作数栈指针
        self.operand_stack = OperandStack(max_stack)
        self.next_pc = 0