"""
问题：定义一个函数，接收一个整数，若该整数为偶数则打印 "It is an even number"，
否则打印 "It is an odd number"。

提示：使用 % 运算符判断奇偶性。
"""

def is_even_number(num):
    if(num % 2 == 0):
        print("It is an even number")
    else:
        print("It is an odd number")


# 测试用例

is_even_number(102)

print('-' *10)

is_even_number(11)