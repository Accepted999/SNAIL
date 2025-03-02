#启动文件，管理工程信息，启动流程

from SNAIL import creat_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# 创建flask的应用对象
app = creat_app("develop")
print(app)
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    # 使用命令启动
    #manager.run()
    #右键manage.py运行
    app.run(host='0.0.0.0', port=5000)
