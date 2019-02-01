import json

import qrcode
from flask import Flask, render_template, url_for, request, session, redirect, g
from flask_login import login_required, LoginManager

from models import User,Case
from exts import db


from earth_after.plu_img import plu_data

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
# login_manager = LoginManager()
# login_manager.init_app(app)


@app.route('/test', methods=['GET', 'POST'])
def test():
        return render_template('tool/generateplu.html')


@app.route('/', methods=['GET', 'POST'])
# @login_required
def index():

    if hasattr(g,'user_name'):
        # return {'user': g.user_name}
    #     return render_template('login.html')
    # else:
    #     return render_template('index.html')
        return render_template('index.html')
    else:
        return render_template('login.html')

    # return render_template ('index.html')
# @app.route('/index', methods=['GET', 'POST'])
# def index1():
#     # if session.get("user_id") != "1":
#     #     return render_template('login.html')
#     # else:
#     #     return render_template('index.html')
#     return render_template('login.html')


@app.route('/testcase/', methods=['GET', 'POST'])
# @login_required
def testcase():
    if request.method == 'GET':
        case = Case.query.filter().all()
        # print(user[0].user_id)
        # user = user[0]
        # data ={
        #     "id":user.user_id,
        #     "name":user.user_name,
        #     'pwd':user.user_password
        # }
        # form = NameForm()
        # return render_template('case/testcase.html',data=data)
        # for k,v in range(len(user)):
        #     print(k,'：',v)
        return render_template('case/testcase.html',content=case)
    else:
        exceldata = request.form.get('exceldata')
        id_list = eval(exceldata)

        for index in id_list:
            # print (type (index))
            # print(eval(index))
            values = list(index.values())
            case1 = Case(own_project=values[1], functional_module=values[2],case_title=values[3],priority=values[4],
                         front_term=values[5],case_description=values[6],expect_result=values[7],remarks=values[11])
            # case.append(case)
            db.session.add(case1)
            db.session.commit ()
            # print(index[0],values)
        data ={
            "status": "1",
            "msg": "导入成功"
        }

        # a = [1, 2, 3, 4, 5, 6]
        # b = [6, 7, 8, 9, 0, 1]
        #
        # # user = User (user_name=name, user_password=pwd)
        # # db.session.add (user)
        # # db.session.commit ()  # 提交
        # hehe_list = [hehe (a=str (a[i]), b=str (b[i])) for i in range (6)]
        # db.session.add_all (hehe_list)
        # db.session.commit ()

        return json.dumps(data)
#
# @app.route('/search/')
# def search():
#     q = request.args.get('q')
#     qustions


@app.route('/testscript/', methods=['GET', 'POST'])
# @login_required
def testscript():

    return render_template('case/testscript.html')


@app.route('/testscriptgroup/', methods=['GET', 'POST'])
# @login_required
def testscriptgroup():
    return render_template ('case/testscriptgroup.html')


@app.route ('/generateplu/', methods=['GET', 'POST'])
def generateplu():
# @app.route ('/generateplu/', methods=['GET', 'POST'])
# # @login_required
# def generateplu():
    if request.method == 'GET':
        return render_template('tool/generateplu.html', content='')
    else:
        skuid = request.form.get('skuid')
        weight = request.form.get('weight')
        plucode = plu_data(skuid, weight)
        # img = qrcode.make (plucode)
        # img.save ("E:/Some.png")
        pludata = {
            "status": "1",
            "plucode": plucode
        }

        # return json.dumps(pludata)
        return render_template ('tool/generateplu.html',content=pludata)


# @app.route ('/generateplu/<plucode>', methods=['GET', 'POST'])
# def generateplu(plucode):
#     if request.method == 'POST':
#         return render_template('tool/generateplu.html',plucode=plucode)


@app.route('/pickinglack/', methods=['GET', 'POST'])
@login_required
def pickinglack():
    return render_template ('tool/pickinglack.html')


@app.route('/autopicking/', methods=['GET', 'POST'])
# @login_required
def autopicking():
    return render_template ('tool/autopicking.html')


@app.route('/urlpath/', methods=['GET', 'POST'])
# @login_required
def urlpath():
    return render_template ('config/urlpath.html')


@app.route('/databaseconfig/', methods=['GET', 'POST'])
# @login_required
def databaseconfig():
    return render_template ('config/databaseconfig.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['name']
        pwd = request.form['password']
        # 用户验证，如果被注册，就不能再被注册了
        user = User.query.filter(User.user_name == name, User.user_password == pwd).first()
        if user:
            session['user_id'] = user.user_id
            # #如果31天内都不需要登录
            session.permanent = True
            data = {
                "status": "1",
                "msg": "登录成功"
            }
            # return redirect(url_for('index'))
        else:
            data = {
                "status": "0",
                "msg": "用户名或密码错误"
            }
            # return json.dumps(data)
            # return "successCallback" + "(" + json.dumps(data) + ")"
        return json.dumps(data)


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    # session.pop('user_id')
    # del session('user_id')
    session.clear()
    return redirect(url_for('login'))


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template ('login.html')
    else:
        name = request.form['name']
        pwd = request.form['password']
        # 用户验证，如果被注册，就不能再被注册了
        user = User.query.filter(User.user_name == name).first()
        if user:
            data = {
                "status": "0",
                "msg": "该用户已注册"
            }
        else:
            user = User(user_name=name,user_password=pwd)
            db.session.add(user)
            db.session.commit() #提交
            data={
                "status": "1",
                "msg": "注册成功"
            }
        return json.dumps(data)


@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.user_id == user_id).first()
        if user:
            g.user_name = user.user_name


@app.context_processor
def my_context_processor():
    if hasattr(g,'user_name'):
        return {'user': g.user_name}
    return {}
# @app.context_processor
# def my_context_processor():
#     user_id = session.get('user_id')
#     if user_id:
#         user = User.query.filter(User.user_id == user_id).first()
#         if user:
#             data = {'user': user.user_name}
#         else:
#             data = {'user': "null"}
#         return data


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True, port=8080)

