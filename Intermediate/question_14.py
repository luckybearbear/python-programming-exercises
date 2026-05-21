"""编写一个程序，接受一个句子并计算大写字母和小写字母的数量。假设程序接收到的输入是：Hello world! 然后，输出应该是：UPPER CASE 1 LOWER CASE 9"""

s = input()

d = {"UPPER CASE": 0, "LOWER CASE": 0}
for c in s:
    if c.isupper():
        d["UPPER CASE"] += 1
    elif c.islower():
        d["LOWER CASE"] += 1
    else:
        pass

print(f'UPPER CASE {d["UPPER CASE"]} LOWER CASE {d["LOWER CASE"]}')
