"""
问题：编写一个函数计算 5/0，并使用 try/except 捕获异常。

提示：使用 try/except 捕获异常，可在 finally 块中进行清理操作。
"""

def divide():
    try:
        res = 5 / 0
        print(res)
    except ZeroDivisionError as err:
        print(f"捕获异常：{err}")
    finally:
        print("执行清理操作")

divide()