"""
问题：编写一个程序，接收以逗号分隔的单词序列作为输入，将这些单词按字母顺序排序后，再以逗号分隔的序列形式输出。
假设程序接收到如下输入：without,hello,bag,world
那么输出应当是：bag,hello,without,world

提示：题目中提到的输入数据，默认通过控制台输入获取
"""
# 1.获取控制台输入的逗号分隔单词
words = input('请输入逗号分隔的单词：')

# 2.按逗号分隔成列表
word_list = words.split(',')

# 3.按字母进行排序
word_list.sort()

# 4.用逗号拼接成字符串输出
print(','.join(word_list))


