from flask import Flask
from Config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
import redis
import logging
from logging.handlers import RotatingFileHandler
from SNAIL.utils.commons import ReConverter

#创建了各类对象，暂时不和flask对象绑定到一起
#在工厂模式时，通过init_app()将其绑定
db = SQLAlchemy()    #flask扩展
redis_store = None
csrf = CSRFProtect()


# 日志
logging.basicConfig(level=logging.DEBUG)  # 调试Debug级别
file_log_handler = RotatingFileHandler("SNAIL/logs/log", maxBytes=1024 * 1024 * 10, backupCount=10, encoding="utf-8")   #日志文件最大的大小为100M  最多只保留10份日志文件
# 创建日志记录的格式                 日志等级     输入日志信息的文件名  行数     日志信息
formatter = logging.Formatter("%(levelname)s %(filename)s:%(lineno)d %(message)s")
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_log_handler)


# 工厂模式  创建flask对象
def creat_app(config_name):

    app = Flask(__name__)

    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    db.init_app(app)
    global redis_store
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT, decode_responses=True)
    Session(app)

    csrf.init_app(app)

    app.url_map.converters["re"] = ReConverter

    from SNAIL import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1.0")

    from SNAIL import web_html
    app.register_blueprint(web_html.html)

    return app

