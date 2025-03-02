#通用的组件信息

from werkzeug.routing import BaseConverter
from flask import session, jsonify, g
from SNAIL.utils.response_code import RET
import functools


# 定义正则转换器
class ReConverter(BaseConverter):

    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(ReConverter, self).__init__(url_map)
        # 保存正则表达式
        self.regex = regex


# xrange
def xrange(start, end=None, step=1):
    if end == None:
        end = start
        start = 0
    if step > 0:
        while start < end:
            yield start
            start += step
    elif step < 0:
        while start > end:
            yield start
            start += step
    else:
        return 'step can not be zero'


# 定义的验证登录状态的装饰器，wraps函数的作用是将wrapper内层函数的属性设置为被装饰函数view_func的属性
def login_required(view_func):
    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):

        user_id = session.get("user_id")

        # 如果用户是登录
        if user_id is not None:
            # 将user_id保存到g对象中
            g.user_id = user_id
            return view_func(*args, **kwargs)
        else:
            return jsonify(errno=RET.SESSIONERR, errmsg="用户未登录")

    return wrapper
