"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 10:15
*  @Project :   JVMbyPython
*  @desc    :   按位或(or)指令
**************************************
"""
from ch05.instructions.base.Instruction import NoOperandsInstruction
from ch05.rtda import Frame


def _or(frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_numeric()
    v1 = stack.pop_numeric()
    result = v1 | v2
    stack.push_numeric(result)


# int or
class IOR(NoOperandsInstruction):
    def execute(self, frame):
        _or(frame)


# long or
class LOR(NoOperandsInstruction):
    def execute(self, frame):
        _or(frame)