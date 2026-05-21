"""
题目：编写程序，接收以空格分隔的一串单词作为输入，去除所有重复单词后，再按字母数字顺序排序并输出。
示例输入：hello world and practice makes perfect and hello world again
对应输出：again and hello makes perfect practice world
提示：题目所给输入数据均默认从控制台录入。可利用集合自动去重，再用sorted()函数完成排序。
"""
s = input()

words = s.split(" ")

print(" ".join(sorted(list(set(words)))))