"""
问题：编写程序，使用 map() 函数生成列表 [1,2,3,4,5,6,7,8,9,10] 中各元素的平方，并打印结果。

提示：
- 使用 map() 生成新列表。
- 使用 lambda 定义匿名函数。
- 注意：Python 3 中 map() 返回迭代器，需用 list() 转换后打印。
"""

init_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = map(lambda x: x**2, init_list)

print(list(res))
