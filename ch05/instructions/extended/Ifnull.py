"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 10:48
*  @Project :   JVMbyPython
*  @desc    :   根据引用是否为null进行跳转
**************************************
"""
from ch05.instructions.base.BranchLogic import branch
from ch05.instructions.base.Instruction import BranchInstruction


class IFNULL(BranchInstruction):
    def execute(self, frame):
        ref = frame.operand_stack.pop_ref()
        if ref is None:
            branch(frame, self.offset)


class IFNONNULL(BranchInstruction):
    def execute(self, frame):
        ref = frame.operand_stack.pop_ref()
        if ref:
            branch(frame, self.offset)