"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/31 14:50
*  @Project :   JVMbyPython
*  @desc    :   Java虚拟机栈
**************************************
"""

from ch04.rtda import Frame

class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.__top = None

    # 把帧推入栈顶
    def push(self, frame: Frame):
        # 如果栈已经满了，抛出StackOverflowError异常
        if self.size >= self.max_size:
            raise RuntimeError("java.lang.StackOverflowError")
        if self.__top:
            frame.lower = self.__top
        self.__top = frame
        self.size += 1

    # 把栈顶帧弹出
    def pop(self) -> Frame:
        if self.__top is None:
            raise RuntimeError("jvm stack is empty!")

        top = self.__top
        self.__top = top.lower
        top.lower = None
        self.size -= 1

        return top

    # 返回栈顶帧，但并不弹出
    def top(self):
        if self.__top is None:
            raise RuntimeError("jvm stack is empty!")

        return self.__top