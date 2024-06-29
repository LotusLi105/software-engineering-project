from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import mysql.connector

app = Flask(__name__)
# 配置数据库连接
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'rjgc'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

# 首页
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    # 查询鱼的种类和数量
    fish_query = "SELECT *  FROM fish "
    cursor.execute(fish_query)
    fish_data = cursor.fetchall()
    # 转换数据为字典列表
    fish_info = []
    for entry in fish_data:
        fish_info.append({
            'Species': entry[0],
            'Weight(g)': entry[1],
            'Length1(cm)': entry[2],
            'Length2(cm)': entry[3],
            'Length3(cm)': entry[4],
            'Height(cm)': entry[5],
            'Width(cm)': entry[6]
        })

    cursor.close()
    conn.close()
    return render_template('maininfo.html', fish_info=fish_info)


# 登录页面
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 处理用户提交的登录表单
        username = request.form.get('username')
        password = request.form.get('password')

        # 在这里进行登录验证的逻辑判断
        if username == 'admin' and password == '123456':
            return redirect(url_for('maininfo'))  # 登录成功，跳转到仪表盘页面
        else:
            error = '用户名或密码错误，请重新登录'
            return render_template('login.html', error=error)

    return render_template('login.html')

# 主要信息页面
@app.route('/maininfo')
def main_info():
    conn = get_db_connection()
    cursor = conn.cursor()

    # 查询鱼的种类和数量
    fish_query = "SELECT *  FROM fish "
    cursor.execute(fish_query)
    fish_data = cursor.fetchall()
    # 转换数据为字典列表
    fish_info = []
    for entry in fish_data:
        fish_info.append({
            'Species': entry[0],
            'Weight(g)': entry[1],
            'Length1(cm)': entry[2],
            'Length2(cm)': entry[3],
            'Length3(cm)': entry[4],
            'Height(cm)': entry[5],
            'Width(cm)': entry[6]
        })

    cursor.close()
    conn.close()
    return render_template('maininfo.html', fish_info=fish_info)
# 注册页面
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 处理用户提交的注册表单
        username = request.form.get('username')
        password = request.form.get('password')

        # 在这里进行注册逻辑的处理
        # ...

        return redirect(url_for('login'))  # 注册成功，跳转到登录页面

    return render_template('register.html')

# 水下系统页面
@app.route('/underwater')
def underwater():
    return render_template('underwater.html')

# 数据中心页面
@app.route('/datacenter')
def datacenter():
    return render_template('datacenter.html')

# 智能中心页面
@app.route('/smartcenter')
def smartcenter():
    return render_template('smartcenter.html')



if __name__ == '__main__':
    app.run(debug=True)
