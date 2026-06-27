"""
问题：读取一个 ASCII 字符串，并将其以 UTF-8 编码后再解码为 Unicode 字符串并打印。

提示：Python 3 中字符串本身已是 Unicode；可使用 encode() 和 decode() 演示编解码过程。
"""

# 读取输入（Python3 input 得到Unicode字符串，题目假设输入内容仅含ASCII字符）
ascii_text = input()

# 1. Unicode字符串 encode 为utf-8字节流
utf8_bytes = ascii_text.encode("utf-8")
print("UTF-8编码后的字节：", utf8_bytes)

# 2. 将utf-8字节解码回Unicode字符串
unicode_str = utf8_bytes.decode("utf-8")
print("解码后的Unicode字符串：", unicode_str)