'''
'''

from flask import Blueprint, render_template, url_for, request, redirect, session

view_admin = Blueprint('view_admin', __name__, template_folder='templates')

@view_admin.route('/')
def index():
    return render_template('admin.html')
