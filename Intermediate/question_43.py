"""
问题：编写程序，接收字符串输入，如果字符串是 "yes"、"YES" 或 "Yes"，则打印 "Yes"，否则打印 "No"。

提示：使用 if 语句进行条件判断。
"""

input_s = input()

if input_s == "yes" or input_s == "YES" or input_s == "Yes":
    print("Yes")
else:
    print("No")
