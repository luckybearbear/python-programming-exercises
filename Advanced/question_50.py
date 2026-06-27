"""
问题：定义一个名为 American 的类，该类包含一个静态方法 printNationality，调用时打印 "America"。

提示：使用 @staticmethod 装饰器定义类的静态方法。
"""
class American():
    
    @staticmethod
    def printNationality():
        print("America")

American.printNationality()