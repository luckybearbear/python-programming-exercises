"""
问题：编写程序，使用 map() 和 filter() 结合 lambda，生成 1 到 20（含两端）各数的平方列表并打印。
（本题与 question_48 类似，重点练习 map() 与 range() 的组合使用）

提示：
- 使用 map() 生成新列表。
- 使用 lambda 定义匿名函数。
"""
res = map(lambda x : x ** 2, filter(lambda x : x % 2 == 0, range(1, 21)))

print(list(res))