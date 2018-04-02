[TOC]

### 示例flask
#### 1. 创建项目
* pycharm-->file-->new project--Flask
    + localtion: 本地
    + Interpreter: C:\virtualenv\flask\Scripts\python.exe
    + More Settiings: 默认值

#### 2. flask程序代码详细解释
    ```
    #encoding: utf-8
    from flask import Flask

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
    def hello_world():
        return '我是第一个flaski程序'

    # 如果当前这个文件是作为入口程序运行,那么就执行app,run()
    if __name__ == '__main__':
        # 启动一个应用服务器,来接受用户的请求
        # while True:
        #    Listen()
        app.run()
    ```

#### 设置 debug模式:
1. 在app,run()中传入一个关键字参数 debug,app.run(debug=True),就设置当前项目为 debug模式
2. debug模式的两大功能
    * 当程序出现问题的时候,可以在页面中看到错误信息和出错的位置。
    * 只要修改了项目中的 python.文件,程序会自动加载,不需要手动重新启动服务器

#### 使用配置文件:
1. 新建一个confg.py文件
2. 在主app文件中导入这个文件,并且配置到`app中,示例代码如下
    ```
    import config
    app.config.from_object(config)
    ```

3. 还有许多的其他参数,都是放在这个配置文件中,比如 SECRET KEY和5 QLALCHEMY这些配置,都是在这个文件中。

#### urL传争数
* 参数的作用:可以在相同的URL,但是指定不同的参数,来加载不同的id数据。
* 参数需要放在两个尖括号中。
* 视图函数中需要放和ur1中的参数同名的参数。
    ```
    @app.route('/articles/<id>')
    def articles(id):
        return u'请求的参量: %s' % id
    ```

#### 反转URL:
* 从视图函数到u的转换叫做反转url
* 反转urL的用处:
* 在页面重定向的时候,会使用urL反转。
* 在模板中,也会使用urL反转。
    ```
    from flask import url_for
    @app.route('/url_for')
    def url_for_def():
        # index是已定义的def
        print url_for('index')
        print url_for('articles' , id='123')
        return u'url反转'
    ```

#### 页面跳转与重定向:
* 用处：在用户访问一些需要登录的页面时；若用户没有登录，则重定向到登录页面
* 反转urL的用处:
* 在页面重定向的时候,会使用urL反转。
* 在模板中,也会使用urL反转。
    ```
    from flask import redirect
    @app.route('/question/<is_login>')
    def question(is_login):
        if is_login == '1':
            return u'成功页面'
        else:
            return redirect(url_for('index'))
    ```