from flask import Blueprint

bbs_bp = Blueprint("bbs", __name__, url_prefix="/bbs/")

@bbs_bp.route("index")
def index():
    return "bbs index"