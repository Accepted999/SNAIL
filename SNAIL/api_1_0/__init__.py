from flask import Blueprint

# 创建蓝图对象
api = Blueprint("api_1_0", __name__)

# 导入蓝图的视图  使其知道有哪些文件
from SNAIL.api_1_0 import verify_code, passport, profile, houses, orders, pay
