"""
问题：编写一个程序，接受一个句子并计算其中的字母和数字的数量。假设以下输入提供给程序：hello world! 123 然后，输出应该是：字母 10 数字 3
提示：如果输入数据提供给问题，应假设为控制台输入。
"""

s = input()

zm, sz = 0, 0

for c in s:
    if c.isalpha():
        zm += 1
    elif c.isdigit():
        sz += 1

print(f"字母 {zm} 数字 {sz}")
