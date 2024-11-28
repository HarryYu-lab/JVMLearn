"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 10:00
*  @Project :   JVMbyPython
*  @desc    :   float类型变量存储指令
**************************************
"""
from ch05.instructions.base.Instruction import Index8Instruction, NoOperandsInstruction


def _fstore(frame, index):
    val = frame.operand_stack.pop_numeric()
    frame.local_vars.set_numeric(index, val)


class FSTORE(Index8Instruction):
    def execute(self, frame):
        _fstore(frame, self.index)


class FSTORE_0(NoOperandsInstruction):
    def execute(self, frame):
        _fstore(frame, 0)


class FSTORE_1(NoOperandsInstruction):
    def execute(self, frame):
        _fstore(frame, 1)


class FSTORE_2(NoOperandsInstruction):
    def execute(self, frame):
        _fstore(frame, 2)


class FSTORE_3(NoOperandsInstruction):
    def execute(self, frame):
        _fstore(frame, 3)