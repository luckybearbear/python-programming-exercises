"""
问题：定义一个自定义异常类 MyError，该类接收一个字符串消息作为属性。

提示：自定义异常需继承自 Exception 类。
"""
# 自定义异常，继承 Exception
class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """
    def __init__(self, msg):
        # 保存消息为实例属性
        self.msg = msg
        # 调用父类构造
        super().__init__(msg)

# 抛出自定义异常
raise MyError("12")
