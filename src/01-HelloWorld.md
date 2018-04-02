[TOC]

### ʾ��flask
#### 1. ������Ŀ
* pycharm-->file-->new project--Flask
    + localtion: ����
    + Interpreter: C:\virtualenv\flask\Scripts\python.exe
    + More Settiings: Ĭ��ֵ

#### 2. flask���������ϸ����
    ```
    #encoding: utf-8
    from flask import Flask

    # ��ʼ��һ��F1ask����
    # Flaks()
    # ��Ҫ����һ������name
    # 1.����flask���ȥѰ����Դ
    # 2.����flask�������flask-Sqlalchemy���ִ����ʱ��,��ȥѰ���������ڵ�λ��
    app = Flask(__name__)

    # @app. route��һ��װ����
    # @��ͷ,�����ں���������,˵����װ����
    # ���װ����������,����һ��url����ͼ������ӳ��
    # 127.8.8.1:5000/ -->ȥ���� hello_ world�������,Ȼ�󽫽�����ظ������
    @app.route('/')
    def hello_world():
        return '���ǵ�һ��flaski����'

    # �����ǰ����ļ�����Ϊ��ڳ�������,��ô��ִ��app,run()
    if __name__ == '__main__':
        # ����һ��Ӧ�÷�����,�������û�������
        # while True:
        #    Listen()
        app.run()
    ```

#### ���� debugģʽ:
1. ��app,run()�д���һ���ؼ��ֲ��� debug,app.run(debug=True),�����õ�ǰ��ĿΪ debugģʽ
2. debugģʽ��������
    * ��������������ʱ��,������ҳ���п���������Ϣ�ͳ����λ�á�
    * ֻҪ�޸�����Ŀ�е� python.�ļ�,������Զ�����,����Ҫ�ֶ���������������

#### ʹ�������ļ�:
1. �½�һ��confg.py�ļ�
2. ����app�ļ��е�������ļ�,�������õ�`app��,ʾ����������
    ```
    import config
    app.config.from_object(config)
    ```

3. ����������������,���Ƿ�����������ļ���,���� SECRET KEY��5 QLALCHEMY��Щ����,����������ļ��С�

#### urL������
* ����������:��������ͬ��URL,����ָ����ͬ�Ĳ���,�����ز�ͬ��id���ݡ�
* ������Ҫ���������������С�
* ��ͼ��������Ҫ�ź�ur1�еĲ���ͬ���Ĳ�����
    ```
    @app.route('/articles/<id>')
    def articles(id):
        return u'����Ĳ���: %s' % id
    ```

#### ��תURL:
* ����ͼ������u��ת��������תurl
* ��תurL���ô�:
* ��ҳ���ض����ʱ��,��ʹ��urL��ת��
* ��ģ����,Ҳ��ʹ��urL��ת��
    ```
    from flask import url_for
    @app.route('/url_for')
    def url_for_def():
        # index���Ѷ����def
        print url_for('index')
        print url_for('articles' , id='123')
        return u'url��ת'
    ```

#### ҳ����ת���ض���:
* �ô������û�����һЩ��Ҫ��¼��ҳ��ʱ�����û�û�е�¼�����ض��򵽵�¼ҳ��
* ��תurL���ô�:
* ��ҳ���ض����ʱ��,��ʹ��urL��ת��
* ��ģ����,Ҳ��ʹ��urL��ת��
    ```
    from flask import redirect
    @app.route('/question/<is_login>')
    def question(is_login):
        if is_login == '1':
            return u'�ɹ�ҳ��'
        else:
            return redirect(url_for('index'))
    ```