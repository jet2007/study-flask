[TOC]

### 示例flask
#### Flask渲染 Jinja2模板和传参:
1. 如何渲染模板
    - 模板放在 templates文件夹下
```
# templates\index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <p>这是HTML中的文字</p>
    <p>username: {{ username }}</p>
    <p>password: {{ password }}</p>
    <p>age: {{ age }}</p>
    <hr/>

    <p>对象person name: {{ person.name }}</p>
    <p>对象person age: {{ person.age }}</p>
    <p>字典website baidu: {{ websites.baidu }}</p>
    <p>字典website google: {{ websites.google }}</p>
</body>
</html>
```
    - 从 flask`中导入 render template`函数。
    - 在视图函数中,使用 render template函数,渲染模板。注意:只需要填写模板的名字,不需要填写 templates这个文件夹的路径
2. 模板传参:
    * 如果只有一个或者少量参数,直接在 render_template函数中添加关键字参数就可以了。
    * 如果有多个参数的时候,那么可以先把所有的参数放在字典中,然后在 render_template'中使用两个星号,把字典转换成关键参数传递进去,这样的代码更方便管理和使用。

```
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

```

3. 在模板中，如果要使用一个变量，语法 `{{ params }}`
4. 访问模型中的属性或字典，`{{ params.property }}` 或 `{{ params['property'] }}`

#### 控制条件 
```
# templates\condition.html
<!DOCTYPE html>
<html lang="cn">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

    <hr/>
    <p>if判断</p>
    {% if user %}
        <a href="#">{{ user.username }}</a>
        <a href="#">注销</a>
    {% else %}
        <a href="#">登陆</a>
        <a href="#">注册</a>
    {% endif %}

    <hr/>
      {% for digit in digits -%}
        <p>{{ digit }}</p>
      {%- endfor %}
    <hr/>
    <dl>
    {% for user in users if not user.hidden %}
      {% if loop.first %}
        <div>User List:</div>
      {% endif %}
      <div class="{{ loop.cycle('odd', 'even') }}">
      <dt>User No {{ loop.index }}:</dt>
      <dd>{{ user.name }}</dd>
      </div>
      {% if loop.last %}
        <div>Total Users: {{ loop.length }}</div>
      {% endif %}
    {% else %}
      <li>No users found</li>
    {% endfor %}
    </dl>
</body>
</html>
```

- if/loop
```
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



```


#### 控制条件 
- 字符串操作
```
{# 当变量未定义时，显示默认字符串，可以缩写为d #}
<p>{{ name | default('No name', true) }}</p>

{# 单词首字母大写 #}
<p>{{ 'hello' | capitalize }}</p>

{# 单词全小写 #}
<p>{{ 'XML' | lower }}</p>

{# 去除字符串前后的空白字符 #}
<p>{{ '  hello  ' | trim }}</p>

{# 字符串反转，返回"olleh" #}
<p>{{ 'hello' | reverse }}</p>

{# 格式化输出，返回"Number is 2" #}
<p>{{ '%s is %d' | format("Number", 2) }}</p>

{# 关闭HTML自动转义 #}
<p>{{ '<em>name</em>' | safe }}</p>

{% autoescape false %}
{# HTML转义，即使autoescape关了也转义，可以缩写为e #}
<p>{{ '<em>name</em>' | escape }}</p>
{% endautoescape %}
```

- 数值操作
```
{# 四舍五入取整，返回13.0 #}
<p>{{ 12.8888 | round }}</p>

{# 向下截取到小数点后2位，返回12.88 #}
<p>{{ 12.8888 | round(2, 'floor') }}</p>

{# 绝对值，返回12 #}
<p>{{ -12 | abs }}</p>
```
- 列表操作
```
{# 取第一个元素 #}
<p>{{ [1,2,3,4,5] | first }}</p>

{# 取最后一个元素 #}
<p>{{ [1,2,3,4,5] | last }}</p>

{# 返回列表长度，可以写为count #}
<p>{{ [1,2,3,4,5] | length }}</p>

{# 列表求和 #}
<p>{{ [1,2,3,4,5] | sum }}</p>

{# 列表排序，默认为升序 #}
<p>{{ [3,2,1,5,4] | sort }}</p>

{# 合并为字符串，返回"1 | 2 | 3 | 4 | 5" #}
<p>{{ [1,2,3,4,5] | join(' | ') }}</p>

{# 列表中所有元素都全大写。这里可以用upper,lower，但capitalize无效 #}
<p>{{ ['tom','bob','ada'] | upper }}</p>
```
- 字典列表操作
```
{% set users=[{'name':'Tom','gender':'M','age':20},
              {'name':'John','gender':'M','age':18},
              {'name':'Mary','gender':'F','age':24},
              {'name':'Bob','gender':'M','age':31},
              {'name':'Lisa','gender':'F','age':19}]
%}


{# 按指定字段排序，这里设reverse为true使其按降序排 #}
<ul>
{% for user in users | sort(attribute='age', reverse=true) %}
     <li>{{ user.name }}, {{ user.age }}</li>
{% endfor %}
</ul>

{# 列表分组，每组是一个子列表，组名就是分组项的值 #}
<ul>
{% for group in users|groupby('gender') %}
    <li>{{ group.grouper }}<ul>
    {% for user in group.list %}
        <li>{{ user.name }}</li>
    {% endfor %}</ul></li>
{% endfor %}
</ul>

{# 取字典中的某一项组成列表，再将其连接起来 #}
<p>{{ users | map(attribute='name') | join(', ') }}</p>
```
