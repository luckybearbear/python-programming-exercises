"""
问题：定义一个函数，打印一个字典，其中键为 1 到 3（含两端），值为对应键的平方。

提示：
- 使用 dict[key]=value 向字典中添加条目。
- 使用 ** 运算符计算幂次。
"""

def print_square_dict():
    # 创建一个空字典
    num_dict = {}

    # 向字典添加key 1、2、3,值为对应key的平方
    num_dict[1] = 1 ** 2
    num_dict[2] = 2 ** 2
    num_dict[3] = 3 ** 2

    print(num_dict)

print_square_dict()

