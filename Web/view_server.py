'''
针对server角色的蓝图
'''

from flask import Blueprint, render_template

view_server = Blueprint('view_server', __name__, template_folder='templates')


@view_server.route('/')
def index():
    return render_template("index.html")
