"""
问题：定义一个函数，打印一个字典，其中键为 1 到 20（含两端），值为对应键的平方。

提示：
- 使用 dict[key]=value 向字典中添加条目。
- 使用 ** 运算符计算幂次。
- 使用 range() 进行循环。
"""


def print_square_dict():
    num_dict = {}
    for i in range(1, 21):
        num_dict[i] = i**2

    print(num_dict)


print_square_dict()
