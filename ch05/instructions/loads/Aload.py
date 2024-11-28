"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 9:39
*  @Project :   JVMbyPython
*  @desc    :   引用类型变量加载指令
**************************************
"""

from ch05.instructions.base.Instruction import Index8Instruction, NoOperandsInstruction
from ch05.rtda import Frame


def _aload(frame: Frame, index):
    ref = frame.local_vars.get_ref(index)
    frame.operand_stack.push_ref(ref)


class ALOAD(Index8Instruction):
    def execute(self, frame):
        _aload(frame, self.index)


class ALOAD_0(NoOperandsInstruction):
    def execute(self, frame):
        _aload(frame, 0)


class ALOAD_1(NoOperandsInstruction):
    def execute(self, frame):
        _aload(frame, 1)


class ALOAD_2(NoOperandsInstruction):
    def execute(self, frame):
        _aload(frame, 2)


class ALOAD_3(NoOperandsInstruction):
    def execute(self, frame):
        _aload(frame, 3)