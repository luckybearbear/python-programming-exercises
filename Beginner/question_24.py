"""
问题：Python 的每个内置函数都有内置文档字符串。请编写程序，打印若干内置函数（如 abs()、int()、input()）的文档字符串，
并为自定义函数添加文档字符串后一并打印。

提示：使用 __doc__ 属性获取文档字符串。
"""


# 1. 查看系统内置函数文档字符串
def print_builtin_docs(func_list):
    """打印Python内置函数的文档字符串"""
    for func in func_list:
        print(f"===== 内置函数：{func.__name__}() =====")
        # __doc__ 获取文档注释
        print(func.__doc__)
        print("-" * 60)


# 2. 自定义函数，添加文档字符串
def calc_area(radius):
    """
    根据半径计算圆形面积
    :param radius: float/int，圆的半径
    :return: float，圆面积 = π*r²
    """
    import math

    return math.pi * radius**2


def greet(name):
    """
    问候指定姓名用户
    :param name: str，用户姓名
    :return: str，拼接后的问候语句
    """
    return f"Hello, {name}!"


# 主程序入口
if __name__ == "__main__":
    # 需要查看的内置函数列表
    builtin_funcs = [abs, int, input, len]
    print("【系统内置函数文档】")
    print_builtin_docs(builtin_funcs)

    # 自定义函数列表
    custom_funcs = [calc_area, greet]
    print("【自定义函数文档】")
    for fn in custom_funcs:
        print(f"===== 自定义函数：{fn.__name__}() =====")
        print(fn.__doc__)
        print("-" * 60)
