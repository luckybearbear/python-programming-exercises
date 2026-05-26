"""
问题：编写程序，统计输入文本中各单词出现的频率，并按字母顺序排序后输出，格式为"单词:次数"。

示例输入：
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

示例输出：
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

提示：输入数据应假设为控制台输入。
"""

s = input()

# 先分割
words = s.split(" ")

count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

# 按照字母排序
sorted_words = sorted(count.keys())

# 按格式输出
for w in sorted_words:
    print(f"{w}:{count[w]}")
