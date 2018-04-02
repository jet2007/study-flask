#encoding: utf-8

from flask import Flask
from flask import render_template

app = Flask(__name__)

# 模板
@app.route('/')
def index():

    class Person(object):
        name = 'james'
        age = 18

    p=Person()

    context = {
        'username': u'tommy',
        'password': u'paaaadfd',
        'age': 123,
        # 对象
        'person': p,
        # 字典
        'websites': {
            'baidu': 'www.baidu.com',
            'google': 'www.google.com'
        }
    }

    return render_template('index.html', **context)


# if判断
@app.route('/if/<is_login>')
def if_is_login(is_login):
    if is_login == '1':
        user = {
            'username': 'tom',
            'age': 23
        }
        digits = [1, 2, 3, 4, 5]
        users = [{'name': 'John'},
                 {'name': 'Tom','hidden': True},
                 {'name': 'Lisa'},
                 {'name': 'Bob'}
                 ]

        return render_template('condition.html', user=user, users=users, digits=digits)
    else:
        return render_template('condition.html')


@app.route('/filter/')
def filterss():
    return render_template('filter.html')


if __name__ == '__main__':
    app.run(debug=True)
