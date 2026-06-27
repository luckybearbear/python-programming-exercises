"""
问题：定义一个函数，接收两个以字符串形式传入的整数，计算它们的和并在控制台打印。

提示：使用 int() 将字符串转换为整数。
"""


def add_str_num(num1_str, num2_str):
    # 将字符串转为整数
    num1 = int(num1_str)
    num2 = int(num2_str)
    # 计算和
    total = num1 + num2
    # 控制台打印结果
    print(total)

# 测试示例
add_str_num("123", "456")
add_str_num("-10", "20")