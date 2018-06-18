'''
'''

from flask import Blueprint, render_template, url_for, request, redirect, session

import TaskManager
import NodeManager

view_admin = Blueprint('view_admin', __name__, template_folder='templates')

TM = TaskManager.TaskManager()
NM = NodeManager.NodeManager()


@view_admin.route('/')
def index():
    return render_template('admin.html')


@view_admin.route('/init_database')
def init_database():
    TM.init_db()
    NM.init_db()
    return redirect(url_for("view_admin.index"))

