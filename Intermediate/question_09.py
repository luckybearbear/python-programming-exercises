"""
题目：编写一个程序，接收多行输入内容，将句子中所有字符转为大写后再逐行输出。
假设程序输入如下内容：
Hello worldPractice 
makes perfect

则程序输出结果为：
HELLO WORLDPRACTICE
MAKES PERFECT

提示：若题目给出输入数据，默认从控制台获取输入。
"""
# 创建空列表存放输入的每行内容
lines = []

# 循环读取输入，直到输入空行
while True:
    line = input()
    if not line:
        break
    lines.append(line)

# 把每一行转成大写并输出
for line in lines:
    print(line.upper())