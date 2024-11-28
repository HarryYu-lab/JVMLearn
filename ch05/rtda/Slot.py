"""
**************************************
*  @Author  ：   HarryYu
*  @Time    ：   2024/10/31 15:58
*  @Project :   JVMbyPython
*  @desc    :   Slot类，可以容纳一个int值和一个引用值
**************************************
"""

class Slot():
    def __init__(self):
        # 存放整数
        self.num = 0
        # 存放引用
        self.ref = None

    def __str__(self):
        return "num:{0} ref:{1}".format(self.num, self.ref)