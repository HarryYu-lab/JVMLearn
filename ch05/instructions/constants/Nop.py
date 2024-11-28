"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/6 14:26
*  @Project :   JVMbyPython
*  @desc    :   nop指令，它什么也不做
**************************************
"""
from ch05.instructions.base.Instruction import NoOperandsInstruction


class NOP(NoOperandsInstruction):
    def execute(self, frame):
        # 什么也不用做
        pass