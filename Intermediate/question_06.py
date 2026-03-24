"""
编写程序，根据公式计算并输出值：Q = √[(2 * C * D) / H]
固定值：
C = 50
H = 30
D 是逗号分隔的输入数字（例如输入：100,150,180）输出结果要四舍五入取整数，并用逗号分隔输出。

示例输入：100,150,180

示例输出：18,22,24
"""

import math

# 固定值
C = 50
H = 30

input_str = input()
d_list = input_str.split(",")

r = []

for i in d_list:
    i = int(i)
    q = math.sqrt(2 * C * i / H)
    q_round = round(q)
    r.append(str(q_round))

print(','.join(r))