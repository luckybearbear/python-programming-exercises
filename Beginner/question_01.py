"""问题：写一个程序，找出所有能被7整除但不是5的倍数的数字，范围介于2000到3200之间（两者都包括在内）。获得的数字应以逗号分隔的顺序在单行印刷。"""

def solution():
    """找出2000到3200之间被7整除但不是5的倍数的数字，并用逗号分割打印"""
    result = []
    for num in range(2000, 3201):
        if num % 7 == 0 and num % 5 != 0:
            result.append(str(num))

    print(','.join(result))

if __name__ == "__main__":
    solution()