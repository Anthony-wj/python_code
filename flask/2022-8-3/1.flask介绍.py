'''
    flask: Python中的web框架
    flask :         Django
    轻              重(下载下来就集成了很多东西)
    灵活            固定样式
    api开发比较好    内容系统比较好
'''

'''
    环境准备：
    pycharm
    xshell
    postman
    创建一个虚拟环境 
    

'''
'''
    虚拟环境：
        使用:可以为每个程序创建自己的虚拟环境，每个虚拟环境都是独立运行的
        在git bash中进入虚拟环境：
            mkdir xsfh_flask
            cd xsfh_flask
            python -m venv myvenv # 执行完后会产生一个myenv目录
            source myvenv/Scripts/activate #执行后当前bash就会进入虚拟环境
        linux中进入虚拟环境：
            [root@Seesunman ~]# mkdir /myenv
            [root@Seesunman ~]# cd /myenv/
            [root@Seesunman myenv]# python3 -m venv myvenv
            [root@Seesunman myenv]# cd myvenv/
            [root@Seesunman myvenv]# source bin/activate
            (myvenv) [root@Seesunman myvenv]# 
        pycharm 虚拟解释器选择:
            settings -->Python Interpreter -->add -->选择虚拟环境Scripts路径下的python.exe
'''

'''
    http超文本传输协议
    1991年发布0.9版本，只有GET方法
    1996年，http/1.0版本发布，引入了POST和HEAD等命令
    1997年，发布了http/1.1版本，引入了持久连接
    2009年，谷歌公开了自行研发的SPDY协议
    2015年，HTTP/2发布      多路复用
    
HTTP方法：
GET 请求网页信息  查
POST 提交信息    增
PUT 修改信息     改
DELETE 删除信息  删
'''

# WSGI web server gateway interface
# 是python语言定义的web服务器和web应用程序或者框架之间一张简单而通用的接口规范
# 一般使用gunicorn服务器   --wsgi  --flask


'''
flask 
    微框架
     flask自由，灵活   可扩展性强
     入门简单，适合api开发
'''