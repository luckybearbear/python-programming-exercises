"""
题目要求

编写一个程序，将 `(name, age, height)` 元组按升序排序，其中 `name` 是字符串，`age` 和 `height` 是数字。元组通过控制台输入。

排序规则：
1. 首先按 name（姓名） 排序
2. 然后按 age（年龄） 排序
3. 最后按 score（分数/身高） 排序

优先级顺序： name > age > score（即 name 优先级最高，age 次之，score 最低）

示例输入：
```
Tom,19,80
John,20,90
Jony,17,19
Jony,17,2
Json,21,85
```
预期输出：
```python
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
```
提示

- 输入数据应假设为控制台输入
- 使用 `itemgetter` 来实现多关键字排序
"""
from operator import itemgetter

def main():
    # 读取控制台输入，直到空行结束
    data = []
    while True:
        try:
            line = input().strip()
            if not line:
                break
            # 按逗号分割，去除空格
            parts = [p.strip() for p in line.split(',')]
            name, age, score = parts[0], int(parts[1]), int(parts[2])
            data.append((name, age, score))
        except (EOFError, ValueError):
            break
    
    # 使用 itemgetter 按 name, age, score 排序（默认升序）
    result = sorted(data, key=itemgetter(0, 1, 2))
    
    # 输出为字符串格式（与题目示例一致）
    output = [(str(name), str(age), str(score)) for name, age, score in result]
    print(output)

if __name__ == '__main__':
    main()

