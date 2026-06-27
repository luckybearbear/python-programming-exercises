"""
问题：对于给定元组 (1,2,3,4,5,6,7,8,9,10)，编写程序生成并打印一个新元组，其中只包含原元组中的偶数。

提示：
- 使用 for 循环遍历元组。
- 使用 tuple() 将列表转换为元组。
"""
init_tuple = (1,2,3,4,5,6,7,8,9,10)
even_list = []
for i in init_tuple:
    if(i % 2 == 0):
        even_list.append(i)

print(tuple(even_list))