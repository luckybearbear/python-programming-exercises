"""
问题：定义一个名为 Rectangle 的类，通过长和宽构造，并包含一个计算矩形面积的方法。

提示：使用 def 方法名(self) 定义实例方法。
"""


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


# 测试用例
r = Rectangle(100, 20)
print(f"矩形的面积：{r.get_area()}")
