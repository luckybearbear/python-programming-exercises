"""
问题：定义一个函数，接收两个字符串，打印其中较长的那个字符串。
若两个字符串长度相同，则逐行打印所有字符串。

提示：使用 len() 函数获取字符串长度。
"""

def print_longer_str(str1, str2):
    str1_length = len(str1)
    str2_length = len(str2)

    if(str1_length == str2_length):
        print(str1 +'\n' +str2)
    elif(str1_length > str2_length):
        print(str1)
    else:
        print(str2)

# 测试示例
print_longer_str("1","22")
print("-" * 10)
print_longer_str("22","33")
print("-" * 10)
print_longer_str('1', '333')