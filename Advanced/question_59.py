"""
问题：假设邮件地址格式为 "用户名@公司名.com"，用户名和公司名均只由字母组成。
请编写程序，从控制台读取一个邮件地址，并打印其中的公司名部分。

示例输入：john@google.com
示例输出：google

提示：使用 \\w 匹配字母，使用 re 模块的正则表达式提取。
"""

import re

email = input()

# 正则匹配：@后面 .com前面的字母部分
pattern = r"(\w+)@(\w+)\.com"

match = re.match(pattern, email)

if match:
    print(match.group(2))
