"""
问题：编写程序，使用 filter() 函数过滤列表 [1,2,3,4,5,6,7,8,9,10] 中的偶数并打印。

提示：
- 使用 filter() 过滤列表元素。
- 使用 lambda 定义匿名函数。
- 注意：Python 3 中 filter() 返回迭代器，需用 list() 转换后打印。
"""
init_list = [1,2,3,4,5,6,7,8,9,10]

res = filter(lambda x:x % 2 == 0, init_list)

print(list(res))