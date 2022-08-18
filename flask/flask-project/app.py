import os
from flask import Flask
def create_app(config=None):
    app = Flask(__name__)
    #支持不同种方式的配置加载
    #load default configuration
    app.config.from_object('config.settings')

    #根据系统环境变量，加载不同的配置文件
    if 'FLASK_CONF' in  os.environ:
        app.config.from_envvar('FLASK_CONF')

    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith(".py"):
            app.config.form_pyfile(config)

    # 注册路由
    import router
    router.init_app(app)

    # 注册模型
    import model
    model.init_app(app)
    return app