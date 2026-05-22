"""
问题：编写一个程序，根据从控制台输入的交易日志计算银行账户的净金额。

每行输入一笔交易，D 表示存款，W 表示取款，格式如下：
D 100
W 200
输入空行结束。

示例输入：
D 300
D 300
W 200
D 100
（空行）

输出：500
"""

netAmount = 0

while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation == "D":
        netAmount += amount
    elif operation == "W":
        netAmount -= amount
    else:
        pass

print(netAmount) 