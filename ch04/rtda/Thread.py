"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/31 14:49
*  @Project :   JVMbyPython
*  @desc    :   每个实例开的私有线程
**************************************
"""
from ch04.rtda.Stack import Stack

class Thread:
    def __init__(self):
        self.pc = 0
        self.stack = Stack(1024)

    def push_frame(self, frame):
        self.stack.push(frame)

    def pop_frame(self):
        return self.stack.pop()

    @property
    def current_frame(self):
        return self.stack.top()