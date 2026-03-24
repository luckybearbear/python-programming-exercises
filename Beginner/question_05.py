"""
问题：定义一个类，至少有两个方法：getString： 从控制台输入 printString： 获取字符串，打印大写字符串。还请包含简单的测试函数来测试类方法。
提示：使用 init 方法构造一些参数
"""


class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())


strObj = InputOutString()
strObj.getString()
strObj.printString()