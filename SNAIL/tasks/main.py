from celery import Celery
from SNAIL.tasks import config

# 定义celery对象
celery_app = Celery("SNAIL")

# 引入配置信息
celery_app.config_from_object(config)

# 自动搜寻异步任务
celery_app.autodiscover_tasks(["SNAIL.tasks.sms"])
# celery开启的命令
# celery -A SNAIL.tasks.main worker -l info -P eventlet
