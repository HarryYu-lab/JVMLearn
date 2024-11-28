"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 10:00
*  @Project :   JVMbyPython
*  @desc    :   int类型变量存储指令
**************************************
"""
from ch05.instructions.base.Instruction import Index8Instruction, NoOperandsInstruction


def _istore(frame, index):
    val = frame.operand_stack.pop_numeric()
    frame.local_vars.set_numeric(index, val)


class ISTORE(Index8Instruction):
    def execute(self, frame):
        _istore(frame, self.index)


class ISTORE_0(NoOperandsInstruction):
    def execute(self, frame):
        _istore(frame, 0)


class ISTORE_1(NoOperandsInstruction):
    def execute(self, frame):
        _istore(frame, 1)


class ISTORE_2(NoOperandsInstruction):
    def execute(self, frame):
        _istore(frame, 2)


class ISTORE_3(NoOperandsInstruction):
    def execute(self, frame):
        _istore(frame, 3)