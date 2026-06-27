"""
问题：定义一个名为 Circle 的类，通过半径构造，并包含一个计算圆面积的方法。

提示：使用 def 方法名(self) 定义实例方法。
"""

import math


class Circle:
    # 构造方法，接收半径
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        # 圆面积公式：πr²
        return math.pi * self.radius ** 2
    

# 测试示例
c = Circle(1)
print(c.get_area())