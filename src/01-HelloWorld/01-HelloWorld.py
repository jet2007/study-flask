#encoding: utf-8

from flask import Flask
from flask import url_for
from flask import redirect

# 初始化一个F1ask对象
# Flaks()
# 需要传递一个参数name
# 1.方便flask框架去寻找资源
# 2.方便flask插件比如flask-Sqlalchemy出现错误的时候,好去寻找问题所在的位置
app = Flask(__name__)

# @app. route是一个装饰器
# @开头,并且在函数的上面,说明是装饰器
# 这个装饰器的作用,是做一个url与视图函数的映射
# 127.8.8.1:5000/ -->去请求 hello_ world这个函数,然后将结果返回给浏览器
@app.route('/')
def index():
    return '我是第一个flaski程序'


# 参数的作用:可以在相同的URL,但是指定不同的参数,来加载不同的id数据。
@app.route('/articles/<id>')
def articles(id):
    return u'请求的参量: %s' % id


# 反转URL:从视图函数到u的转换叫做反转url
# 反转urL的用处:
# 在页面重定向的时候,会使用urL反转。
# 在模板中,也会使用urL反转。
@app.route('/url_for')
def url_for_def():
    print url_for('index')
    print url_for('articles', id='123')
    return u'url反转'

# 重定向
@app.route('/question/<is_login>')
def question(is_login):
    if is_login == '1':
        return u'成功页面'
    else:
        return redirect(url_for('index'))

# 如果当前这个文件是作为入口程序运行,那么就执行app,run()
if __name__ == '__main__':
    # 启动一个应用服务器,来接受用户的请求
    # while True:
    #    Listen()
    app.run(debug=True)
