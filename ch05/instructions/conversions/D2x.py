"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 10:29
*  @Project :   JVMbyPython
*  @desc    :   double类型转换指令
**************************************
"""
import ctypes

from ch05.instructions.base.Instruction import NoOperandsInstruction


# Convert double to float
class D2F(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        d = stack.pop_numeric()
        f = ctypes.c_float(d).value
        stack.push_numeric(f)


# Convert double to int
class D2I(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        d = stack.pop_numeric()
        i = ctypes.c_int32(d).value
        stack.push_numeric(i)


# Convert double to long
class D2L(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        d = stack.pop_numeric()
        l = ctypes.c_int64(d).value
        stack.push_numeric(l)