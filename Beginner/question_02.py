"""问题：编写一个程序，能够计算给定数字的阶乘。结果应以逗号分隔的序列打印在单行上。假设向程序输入为8，那么输出应为：40320"""


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


x = int(input())
print(fact(x))
