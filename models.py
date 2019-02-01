from exts import db


class User (db.Model):
    __tablename__ = 'test_user'
    user_id = db.Column (db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column (db.String(20), unique=True, nullable=False)
    user_password = db.Column (db.String(40), nullable=False)
    # def __repr__(self): #__repr__方法告诉Python如何打印class对象，方便我们调试使用。
    #     return '<User %r>' % (self.user_id)


class Case (db.Model):
    __tablename__ = 'test_case'
    id = db.Column (db.Integer, primary_key=True,autoincrement=True)
    case_code = db.Column (db.String(20),nullable=False,unique=True)
    own_project = db.Column (db.String(20),nullable=True)
    functional_module = db.Column (db.String(20),nullable=True)
    priority = db.Column(db.Integer, nullable=True) #优先级
    batch_type = db.Column (db.String(20),nullable=True)
    order_type = db.Column (db.String(20),nullable=True)
    goods_type = db.Column (db.String(40),nullable=True)
    front_term = db.Column (db.String(100),nullable=True)  # 前置条件
    case_title = db.Column(db.String(20), nullable=True)
    case_description= db.Column (db.String(500),nullable=True)
    goods_name = db.Column (db.String(40),nullable=True)
    expect_result = db.Column (db.String(500),nullable=True)
    execute_result = db.Column (db.String(10),nullable=True,default='未执行')
    executive = db.Column (db.Integer, db.ForeignKey ("test_user.user_id"))  # 执行人
    creator = db.Column (db.Integer, db.ForeignKey ("test_user.user_id"))  # 创建人
    remarks = db.Column (db.String(100),nullable=True)
    execute_log = db.Column (db.String(500),nullable=True)
    del_flag = db.Column (db.Boolean(),default=False)
    # 创建一个外键，和django不一样。flask需要指定具体的字段创建外键，不能根据类名创建外键



