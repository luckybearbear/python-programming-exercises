"""
问题：定义一个类，该类同时拥有一个类参数（class parameter）和一个同名的实例参数（instance parameter）。

提示：
- 实例参数需要在 __init__ 方法中定义。
- 可以在构造时传入参数，也可以在构造后再赋值。

核心知识点：
- 类参数：直接定义在类体中的变量，属于"类"本身，所有实例共享。
- 实例参数：在 __init__ 中通过 self.xxx 定义的变量，属于"各个实例"。
- 当两者同名时，实例属性会"遮蔽"（shadow）类属性：通过实例访问优先拿到实例属性，
  通过类名访问则始终拿到类属性。
"""


class Person:
    # 类参数（class parameter）：写在类体中，所有实例共享
    name = "Person 类的默认 name"

    def __init__(self, name=None):
        # 实例参数（instance parameter）：写在 __init__ 中，属于每个实例自己
        # 只有构造时传入了 name，才会创建同名的实例属性（从而遮蔽类属性）
        if name is not None:
            self.name = name


if __name__ == "__main__":
    # 1. 不传参构造：实例没有自己的 name，访问到的其实是类参数
    p1 = Person()
    print(f"p1.name        = {p1.name}")   # Person 类的默认 name

    # 2. 构造时传入参数：创建同名实例属性，遮蔽类属性
    p2 = Person("张三")
    print(f"p2.name        = {p2.name}")   # 张三

    # 3. 构造后再赋值：同样会创建实例属性
    p1.name = "李四"
    print(f"p1.name        = {p1.name}")   # 李四

    # 4. 通过类名访问的始终是类参数，不受实例影响
    print(f"Person.name    = {Person.name}")  # Person 类的默认 name

    print("-" * 50)
    print("结论：实例属性一旦创建，就遮蔽同名类属性；但不影响类属性本身。")
