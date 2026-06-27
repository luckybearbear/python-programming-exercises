"""
问题：定义一个函数，生成 1 到 20（含两端）各数的平方列表，并打印其中最后 5 个元素。

提示：
- 使用 ** 运算符计算幂次。
- 使用 range() 进行循环。
- 使用 list.append() 向列表添加元素。
- 使用 [n1:n2] 对列表进行切片。
"""


def print_list():
    num_list = []
    for i in range(1, 21):
        num_list.append(i**2)
    print(num_list[-5:])


print_list()