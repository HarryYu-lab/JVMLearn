"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 10:36
*  @Project :   JVMbyPython
*  @desc    :   比较float变量指令，当两个float变量中至少有一个是NaN时，用fcmpg指令比较的结果是1，用fcmpl指令比较的结果是-1
**************************************
"""

from ch05.instructions.base.Instruction import NoOperandsInstruction


def _fcmp(frame, gFlag):
    stack = frame.operand_stack
    v2 = stack.pop_numeric()
    v1 = stack.pop_numeric()
    if v1 > v2:
        stack.push_numeric(1)
    elif v1 == v2:
        stack.push_numeric(0)
    elif v1 < v2:
        stack.push_numeric(-1)
    elif gFlag:
        stack.push_numeric(1)
    else:
        stack.push_numeric(-1)


class FCMPG(NoOperandsInstruction):
    def execute(self, frame):
        _fcmp(frame, True)


class FCMPL(NoOperandsInstruction):
    def execute(self, frame):
        _fcmp(frame, False)
