"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 9:39
*  @Project :   JVMbyPython
*  @desc    :    int变量加载指令
**************************************
"""

from ch05.instructions.base.Instruction import Index8Instruction, NoOperandsInstruction
from ch05.rtda import Frame


def _iload(frame: Frame, index):
    val = frame.local_vars.get_numeric(index)
    frame.operand_stack.push_numeric(val)


class ILOAD(Index8Instruction):
    def execute(self, frame):
        _iload(frame, self.index)


class ILOAD_0(NoOperandsInstruction):
    def execute(self, frame):
        _iload(frame, 0)


class ILOAD_1(NoOperandsInstruction):
    def execute(self, frame):
        _iload(frame, 1)


class ILOAD_2(NoOperandsInstruction):
    def execute(self, frame):
        _iload(frame, 2)


class ILOAD_3(NoOperandsInstruction):
    def execute(self, frame):
        _iload(frame, 3)