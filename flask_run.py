import json, os
from datetime import timedelta

from flask import Flask, render_template, url_for, request, session, redirect
from flask import make_response, Response
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta (days=7)
app.config.from_object ('config')
db = SQLAlchemy(app)


# app.config['SECRET_KEY'] = 'hard to guess string'
# # app = Flask (__name__, static_folder='', static_url_path='')



@app.route ('/')
def index():
    # earth_user = User(user_name='aaa',user_password='bbb')
    # db.session.add(earth_user)
    # user1 = User.query.filter_by (user_name='aaa').first () #首先查询到名为aaa的这个用户
    # db.session.delete (user1)
    # user1.user_name = 'fang' # 赋值／修改
    # db.session.commit() #提交
    session['username'] = 'diqiugang'
    # del session['username']
    session.permanent = True
    return render_template ('base.html')


"""index
6.查询名字不等于wang的所有数据[2种方式]  

(1)!=: User.query.filter(User.name!='wang').all()  

(2)not:User.query.filter(not(User.name=='wang')).all()  
"""


@app.route('/testcase/')
# @login_required
def testcase():

    return render_template('case/testcase.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True,port=8081)