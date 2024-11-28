"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 10:29
*  @Project :   JVMbyPython
*  @desc    :   float类型转换指令
**************************************
"""
import ctypes

from ch05.instructions.base.Instruction import NoOperandsInstruction


# Convert float to double
class F2D(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        f = stack.pop_numeric()
        d = ctypes.c_float(f).value
        stack.push_numeric(d)


# Convert float to int
class F2I(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        f = stack.pop_numeric()
        i = ctypes.c_int32(f).value
        stack.push_numeric(i)


# Convert float to long
class F2L(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        f = stack.pop_numeric()
        l = ctypes.c_int64(f).value
        stack.push_numeric(l)