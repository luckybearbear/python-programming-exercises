"""
问题：一个网站要求用户输入用户名和密码进行注册。编写一个程序来检查用户输入的密码的有效性。以下是检查密码的标准：
至少包含一个小写字母[a-z]
至少包含一个数字[0-9]
至少包含一个大写字母[A-Z]
至少包含一个字符[$#@]
交易密码的最小长度：6
交易密码的最大长度：12
你的程序应该接受一系列用逗号分隔的密码，并根据上述标准进行检查。符合标准的密码将被打印，每个密码之间用逗号分隔。示例
如果以下密码作为程序的输入：ABd1234@1,a F1#,2w3E*,2We3345
那么，程序的输出应该是：ABd1234@1
提示：如果问题中提供了输入数据，应假定它是控制台输入。
"""

import re

s = input()

values = []

items = [x for x in s.split(",")]

for i in items:
    if len(i) < 6 or len(i) > 12:
        continue
    else:
        pass

    if not re.search("[a-z]", i):
        continue
    elif not re.search("[0-9]", i):
        continue
    elif not re.search("[A-Z]", i):
        continue
    elif not re.search("[$#@]", i):
        continue
    else:
        pass
    values.append(i)

print(",".join(values))
