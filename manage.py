from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from exts import db
from run import app
from models import User,Case

manager = Manager(app)

#使用Migrate绑定app和db
migrate = Migrate(app, db)
#添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()