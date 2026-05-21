"""
问题：编写一个程序，该程序接受一系列用逗号分隔的4位二进制数作为输入，然后检查它们是否能被5整除。要打印出能被5整除的数字，并以逗号分隔。示例：0100,0011,1010,1001。然后输出应为：1010。注意：假设数据通过控制台输入。
提示：如果问题中提供输入数据，应假设为控制台输入。
"""

s = input()

nums = s.split(",")

values = []
for n in nums:
    intp = int(n, 2)
    print(intp%5)
    if not intp%5:
        values.append(n)

print(",".join(values))