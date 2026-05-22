"""
问题：编写一个程序，计算 a+aa+aaa+aaaa 的值，其中 a 是给定的数字。假设程序接收以下输入：9 然后，输出应该是：11106
提示：如果输入数据被提供给问题，应该假设它是控制台输入。
"""

a = input()
# 用生成器一行搞定：a * i 利用字符串重复生成 a、aa、aaa、aaaa，再逐个转 int 求和。
print(sum(int(a * i) for i in range(1, 5)))

b = "2"
print(b * 2)
