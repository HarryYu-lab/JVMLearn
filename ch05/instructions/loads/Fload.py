"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 9:39
*  @Project :   JVMbyPython
*  @desc    :   float类型变量加载指令
**************************************
"""
from ch05.instructions.base.Instruction import Index8Instruction, NoOperandsInstruction


def _fload(frame, index):
    val = frame.local_vars.get_numeric(index)
    frame.operand_stack.push_numeric(val)


class FLOAD(Index8Instruction):
    def execute(self, frame):
        _fload(frame, self.index)


class FLOAD_0(NoOperandsInstruction):
    def execute(self, frame):
        _fload(frame, 0)


class FLOAD_1(NoOperandsInstruction):
    def execute(self, frame):
        _fload(frame, 1)


class FLOAD_2(NoOperandsInstruction):
    def execute(self, frame):
        _fload(frame, 2)


class FLOAD_3(NoOperandsInstruction):
    def execute(self, frame):
        _fload(frame, 3)