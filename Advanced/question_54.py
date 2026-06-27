"""
问题：定义一个名为 Shape 的类和它的子类 Square。Square 的 __init__ 方法接收边长作为参数。
两个类都有 area() 方法：Shape 的 area() 默认返回 0，Square 的 area() 返回边长的平方。

提示：在子类中定义与父类同名的方法即可实现方法重写（override）。
"""


# 图形基类
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, side):
        Shape.__init__(self)
        self.side = side

    def area(self):
        return self.side**2


print(Square(6).area())
