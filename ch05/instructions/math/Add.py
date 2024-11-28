"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 10:15
*  @Project :   JVMbyPython
*  @desc    :   加法(add)指令
**************************************
"""
from ch05.instructions.base.Instruction import NoOperandsInstruction
from ch05.rtda import Frame


def _add(frame: Frame):
    stack = frame.operand_stack
    v1 = stack.pop_numeric()
    v2 = stack.pop_numeric()
    result = v1 + v2
    stack.push_numeric(result)


# double add
class DADD(NoOperandsInstruction):
    def execute(self, frame):
        _add(frame)


# float add
class FADD(NoOperandsInstruction):
    def execute(self, frame):
        _add(frame)


# int add
class IADD(NoOperandsInstruction):
    def execute(self, frame):
        _add(frame)


# long add
class LADD(NoOperandsInstruction):
    def execute(self, frame):
        _add(frame)