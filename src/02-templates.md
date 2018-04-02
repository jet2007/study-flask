[TOC]

### ʾ��flask
#### Flask��Ⱦ Jinja2ģ��ʹ���:
1. �����Ⱦģ��
    - ģ����� templates�ļ�����
```
# templates\index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <p>����HTML�е�����</p>
    <p>username: {{ username }}</p>
    <p>password: {{ password }}</p>
    <p>age: {{ age }}</p>
    <hr/>

    <p>����person name: {{ person.name }}</p>
    <p>����person age: {{ person.age }}</p>
    <p>�ֵ�website baidu: {{ websites.baidu }}</p>
    <p>�ֵ�website google: {{ websites.google }}</p>
</body>
</html>
```
    - �� flask`�е��� render template`������
    - ����ͼ������,ʹ�� render template����,��Ⱦģ�塣ע��:ֻ��Ҫ��дģ�������,����Ҫ��д templates����ļ��е�·��
2. ģ�崫��:
    * ���ֻ��һ��������������,ֱ���� render_template��������ӹؼ��ֲ����Ϳ����ˡ�
    * ����ж��������ʱ��,��ô�����Ȱ����еĲ��������ֵ���,Ȼ���� render_template'��ʹ�������Ǻ�,���ֵ�ת���ɹؼ��������ݽ�ȥ,�����Ĵ������������ʹ�á�

```
#encoding: utf-8

from flask import Flask
from flask import render_template

app = Flask(__name__)

# ģ��
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
        # ����
        'person': p,
        # �ֵ�
        'websites': {
            'baidu': 'www.baidu.com',
            'google': 'www.google.com'
        }
    }

    return render_template('index.html', **context)


# if�ж�
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

3. ��ģ���У����Ҫʹ��һ���������﷨ `{{ params }}`
4. ����ģ���е����Ի��ֵ䣬`{{ params.property }}` �� `{{ params['property'] }}`

#### �������� 
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
    <p>if�ж�</p>
    {% if user %}
        <a href="#">{{ user.username }}</a>
        <a href="#">ע��</a>
    {% else %}
        <a href="#">��½</a>
        <a href="#">ע��</a>
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


#### �������� 
- �ַ�������
```
{# ������δ����ʱ����ʾĬ���ַ�����������дΪd #}
<p>{{ name | default('No name', true) }}</p>

{# ��������ĸ��д #}
<p>{{ 'hello' | capitalize }}</p>

{# ����ȫСд #}
<p>{{ 'XML' | lower }}</p>

{# ȥ���ַ���ǰ��Ŀհ��ַ� #}
<p>{{ '  hello  ' | trim }}</p>

{# �ַ�����ת������"olleh" #}
<p>{{ 'hello' | reverse }}</p>

{# ��ʽ�����������"Number is 2" #}
<p>{{ '%s is %d' | format("Number", 2) }}</p>

{# �ر�HTML�Զ�ת�� #}
<p>{{ '<em>name</em>' | safe }}</p>

{% autoescape false %}
{# HTMLת�壬��ʹautoescape����Ҳת�壬������дΪe #}
<p>{{ '<em>name</em>' | escape }}</p>
{% endautoescape %}
```

- ��ֵ����
```
{# ��������ȡ��������13.0 #}
<p>{{ 12.8888 | round }}</p>

{# ���½�ȡ��С�����2λ������12.88 #}
<p>{{ 12.8888 | round(2, 'floor') }}</p>

{# ����ֵ������12 #}
<p>{{ -12 | abs }}</p>
```
- �б����
```
{# ȡ��һ��Ԫ�� #}
<p>{{ [1,2,3,4,5] | first }}</p>

{# ȡ���һ��Ԫ�� #}
<p>{{ [1,2,3,4,5] | last }}</p>

{# �����б��ȣ�����дΪcount #}
<p>{{ [1,2,3,4,5] | length }}</p>

{# �б���� #}
<p>{{ [1,2,3,4,5] | sum }}</p>

{# �б�����Ĭ��Ϊ���� #}
<p>{{ [3,2,1,5,4] | sort }}</p>

{# �ϲ�Ϊ�ַ���������"1 | 2 | 3 | 4 | 5" #}
<p>{{ [1,2,3,4,5] | join(' | ') }}</p>

{# �б�������Ԫ�ض�ȫ��д�����������upper,lower����capitalize��Ч #}
<p>{{ ['tom','bob','ada'] | upper }}</p>
```
- �ֵ��б����
```
{% set users=[{'name':'Tom','gender':'M','age':20},
              {'name':'John','gender':'M','age':18},
              {'name':'Mary','gender':'F','age':24},
              {'name':'Bob','gender':'M','age':31},
              {'name':'Lisa','gender':'F','age':19}]
%}


{# ��ָ���ֶ�����������reverseΪtrueʹ�䰴������ #}
<ul>
{% for user in users | sort(attribute='age', reverse=true) %}
     <li>{{ user.name }}, {{ user.age }}</li>
{% endfor %}
</ul>

{# �б���飬ÿ����һ�����б��������Ƿ������ֵ #}
<ul>
{% for group in users|groupby('gender') %}
    <li>{{ group.grouper }}<ul>
    {% for user in group.list %}
        <li>{{ user.name }}</li>
    {% endfor %}</ul></li>
{% endfor %}
</ul>

{# ȡ�ֵ��е�ĳһ������б��ٽ����������� #}
<p>{{ users | map(attribute='name') | join(', ') }}</p>
```
