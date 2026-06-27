"""
问题：定义一个函数，生成并打印一个元组，其中的值为 1 到 20（含两端）各数的平方。

提示：
- 使用 ** 运算符计算幂次。
- 使用 range() 进行循环。
- 使用 list.append() 向列表添加元素。
- 使用 tuple() 将列表转换为元组。
"""


def print_tuple():
    num_list = []
    for i in range(1, 21):
        num_list.append(i**2)
    print(tuple(num_list))


print_tuple()
