'''
'''

from flask import Blueprint, render_template, url_for, request, redirect, session, flash

import server_start

view_admin = Blueprint('view_admin', __name__, template_folder='templates')

TM = server_start.server.task_manager
NM = server_start.server.node_manager
W = server_start.server.web


@view_admin.route('/')
def index():
    return render_template('admin.html')


@view_admin.route('/init_database')
def init_database():
    TM.init_db()
    NM.init_db()
    return redirect(url_for("view_admin.index"))


@view_admin.route('/start_ftp_server')
def start_ftp_server():
    try:
        W.run_ftp_server()
        flash("FTP服务器启动成功")
    except expression as identifier:
        flask("FTP服务器启动失败")
    finally:
        return redirect(url_for("view_admin.index"))
