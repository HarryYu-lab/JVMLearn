"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 10:00
*  @Project :   JVMbyPython
*  @desc    :   引用类型变量存储指令
**************************************
"""
from ch05.instructions.base.Instruction import Index8Instruction, NoOperandsInstruction


def _astore(frame, index):
    ref = frame.operand_stack.pop_ref()
    frame.local_vars.set_ref(index, ref)


class ASTORE(Index8Instruction):
    def execute(self, frame):
        _astore(frame, self.index)


class ASTORE_0(NoOperandsInstruction):
    def execute(self, frame):
        _astore(frame, 0)


class ASTORE_1(NoOperandsInstruction):
    def execute(self, frame):
        _astore(frame, 1)


class ASTORE_2(NoOperandsInstruction):
    def execute(self, frame):
        _astore(frame, 2)


class ASTORE_3(NoOperandsInstruction):
    def execute(self, frame):
        _astore(frame, 3)