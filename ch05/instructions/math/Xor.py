"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 10:16
*  @Project :   JVMbyPython
*  @desc    :   按位异或(xor)指令
**************************************
"""
from ch05.instructions.base.Instruction import NoOperandsInstruction
from ch05.rtda import Frame


def _xor(frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_numeric()
    v1 = stack.pop_numeric()
    result = v1 ^ v2
    stack.push_numeric(result)


# int xor
class IXOR(NoOperandsInstruction):
    def execute(self, frame):
        _xor(frame)


# long xor
class LXOR(NoOperandsInstruction):
    def execute(self, frame):
        _xor(frame)