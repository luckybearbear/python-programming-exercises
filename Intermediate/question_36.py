"""
问题：定义一个函数，生成并打印一个列表，列表中的值为 1 到 20（含两端）各数的平方。

提示：
- 使用 ** 运算符计算幂次。
- 使用 range() 进行循环。
- 使用 list.append() 向列表添加元素。
"""


def print_list():
    num_list = []
    for i in range(1, 21):
        num_list.append(i**2)
    print(num_list)


print_list()
