"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 10:15
*  @Project :   JVMbyPython
*  @desc    :   取反(neg)指令
**************************************
"""
from ch05.instructions.base.Instruction import NoOperandsInstruction


def _neg(frame):
    stack = frame.operand_stack
    val = stack.pop_numeric()
    stack.push_numeric(-val)


# double negate
class DNEG(NoOperandsInstruction):
    def execute(self, frame):
        _neg(frame)


# float negate
class FNEG(NoOperandsInstruction):
    def execute(self, frame):
        _neg(frame)


# int negate
class INEG(NoOperandsInstruction):
    def execute(self, frame):
        _neg(frame)


# long negate
class LNEG(NoOperandsInstruction):
    def execute(self, frame):
        _neg(frame)