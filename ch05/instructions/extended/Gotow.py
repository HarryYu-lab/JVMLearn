"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 10:48
*  @Project :   JVMbyPython
*  @desc    :    goto_w指令和goto指令的唯一区别就是索引从2字节变成了4字节
**************************************
"""
import ctypes

from ch05.instructions.base.BranchLogic import branch
from ch05.instructions.base.Instruction import NoOperandsInstruction


class GOTO_W(NoOperandsInstruction):
    def __init__(self):
        self.offset = 0

    def fetch_operands(self, reader):
        self.offset = ctypes.c_int(reader.read_int32()).value

    def execute(self, frame):
        branch(frame, self.offset)