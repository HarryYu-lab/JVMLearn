"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/11/28 10:43
*  @Project :   JVMbyPython
*  @desc    :   跳转逻辑
**************************************
"""
from ch05.rtda import Frame


def branch(frame: Frame, offset):
    pc = frame.thread.pc
    next_pc = pc + offset
    frame.next_pc = next_pc