"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 10:01
*  @Project :   JVMbyPython
*  @desc    :   long类型变量存储指令
**************************************
"""
from ch05.instructions.base.Instruction import Index8Instruction, NoOperandsInstruction


def _lstore(frame, index):
    val = frame.operand_stack.pop_numeric()
    frame.local_vars.set_numeric(index, val)


class LSTORE(Index8Instruction):
    def execute(self, frame):
        _lstore(frame, self.index)


class LSTORE_0(NoOperandsInstruction):
    def execute(self, frame):
        _lstore(frame, 0)


class LSTORE_1(NoOperandsInstruction):
    def execute(self, frame):
        _lstore(frame, 1)


class LSTORE_2(NoOperandsInstruction):
    def execute(self, frame):
        _lstore(frame, 2)


class LSTORE_3(NoOperandsInstruction):
    def execute(self, frame):
        _lstore(frame, 3)