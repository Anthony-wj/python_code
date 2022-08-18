from .study import study_bp
from .news import news_bp
from .bbs import bbs_bp
from .user import user_bp
def init_app(app):
    app.register_blueprint(study_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(bbs_bp)
    app.register_blueprint(user_bp)
