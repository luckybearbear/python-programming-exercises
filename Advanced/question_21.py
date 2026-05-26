"""
问题：一个机器人从原点 (0,0) 出发，在平面上移动。机器人可以向 UP、DOWN、LEFT、RIGHT 四个方向移动若干步。
移动轨迹示例：
UP 5
DOWN 3
LEFT 3
RIGHT 2
...
方向后面的数字代表步数。请编写程序，根据一系列移动指令计算机器人当前位置与原点的距离。
如果距离是小数，则输出最近的整数。

示例输入：
UP 5
DOWN 3
LEFT 3
RIGHT 2
（空行结束）

示例输出：2

提示：输入数据应假设为控制台输入。
"""

import math

# 初始坐标 (x, y)
pos = [0, 0]

while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])

    # 移动逻辑
    if direction == "UP":
        pos[1] += steps
    elif direction == "DOWN":
        pos[1] -= steps
    elif direction == "LEFT":
        pos[0] -= steps
    elif direction == "RIGHT":
        pos[0] += steps
    else:
        pass

# 最后：计算欧几里得距离
distance = math.sqrt(pos[0] ** 2 + pos[1] ** 2)

# 输出最近的整数（四舍五入）
print(round(distance))
