"""
编写程序，输入两个数字 X，Y，生成一个二维数组。
规则：
第 i 行、第 j 列的元素值 = i * j
行范围：i = 0,1,..., X-1（一共 X 行）
列范围：j = 0,1,..., Y-1（一共 Y 列）
示例：输入：3,5输出：[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""

# 获取输入并转成数字 X, Y
x, y = map(int, input().split(","))

# 创建二维数组
result = []
for i in range(x):
    row = []
    for j in range(y):
        row.append(i * j)
    result.append(row)

# 输出
print(result)
