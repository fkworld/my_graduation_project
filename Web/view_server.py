'''
针对server角色的蓝图
'''

import flask

import server_start

view_server = flask.Blueprint(
    'view_server', __name__, template_folder='templates')


@view_server.route('/')
def index():
    return flask.render_template("index.html")


@view_server.route('/node_manager')
def node_manager():
    node_list = server_start.server.node_manager.show_all_node()
    return flask.render_template('node_manager.html', node_list=node_list)
