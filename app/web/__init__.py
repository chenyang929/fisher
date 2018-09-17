from flask import Blueprint, render_template

web = Blueprint('web', __name__)


# AOP思想
@web.app_errorhandler(404)
def not_found(e):
    # 可以实现任意代码逻辑
    return render_template('404.html'), 404


# 需要导入
from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish

