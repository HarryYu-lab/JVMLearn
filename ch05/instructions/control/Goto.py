"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 10:44
*  @Project :   JVMbyPython
*  @desc    :   goto指令，进行无条件跳转
**************************************
"""
from ch05.instructions.base.BranchLogic import branch
from ch05.instructions.base.Instruction import BranchInstruction


class GOTO(BranchInstruction):
    def execute(self, frame):
        branch(frame, self.offset)