from flask import Flask,request

import pymssql
import json

conn = pymssql.connect('120.79.153.81','sa','Dyd123456','wxapp')


cursor = conn.cursor()


app = Flask(__name__)

#根路由
@app.route('/')
def hello_world():
    return 'Hello Flask!'

#子路由
@app.route('/hello',methods=['GET'])
def hello():
    # 查询操作
    cursor.execute('SELECT * FROM wxuser')

    row = cursor.fetchone()

    users = ""

    # 将数据加入数组
    for row in cursor:
        usr = '{"name":"%s","sex":"%s","creattime":"%s","updatetime":"%s","jf":"%s","school":"%s","openid":"%s"},' % (
        row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        users += usr

    users = '[' + users[:-1] + ']'

    usersjson = json.dumps(users)

    return usersjson
    conn.close()

#路由传参
@app.route('/user/<username>')
def show_name(username):
    return 'User %s' % username

#参数类型定义int、float、path
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'post %s' % post_id

#http请求
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        a = request.get_data()
        dict1 = json.loads(a)
        return json.dumps(dict1)
    else:
        return '<h1>只接受post请求！</h1>'



if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0')