"""
问题：定义一个函数，生成键为 1 到 20（含两端）、值为对应键的平方的字典，并只打印所有的键。

提示：
- 使用 dict[key]=value 向字典中添加条目。
- 使用 ** 运算符计算幂次。
- 使用 range() 进行循环。
- 使用 dict.keys() 获取所有键。
"""


def print_dict_keys():
    num_dict = {}
    for i in range(1, 21):
        num_dict[i] = i**2

    for k in num_dict.keys():
        print(k)


print_dict_keys()
