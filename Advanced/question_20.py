"""
定义一个类，在这个类里实现一个生成器，用于迭代遍历0 到给定数值 n 之间所有能被 7 整除的数字。
提示：考虑使用 yield 关键字
"""
# 定义类
class DivisibleBySeven:
    # 初始化方法，接收上限 n
    def __init__(self, n):
        self.n = n

    # 生成器方法：遍历 0~n 中能被 7 整除的数
    def generate_seven(self):
        for num in range(self.n + 1):  # 包含 n 本身
            if num % 7 == 0:  # 判断是否能被 7 整除
                yield num  # 生成器返回当前数字


# ------------------- 测试代码 -------------------
if __name__ == "__main__":
    # 创建实例，上限设为 50
    obj = DivisibleBySeven(50)
    
    # 遍历生成器输出结果
    print("0 到 50 之间能被 7 整除的数字：")
    for number in obj.generate_seven():
        print(number, end=" ")