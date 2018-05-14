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


@view_server.route('/test')
def test():
    node_list = server_start.server.node_manager.show_all_node()
    node = node_list[0]
    a= flask.url_for('static',filename='example.png')
    print(a)
    return flask.render_template('preview_node.html',node=node)


@view_server.route('/node_manager')
def node_manager():
    node_list = server_start.server.node_manager.show_all_node()
    return flask.render_template('node_manager.html', node_list=node_list)


@view_server.route('/task_manager')
def task_manager():
    task_list = server_start.server.task_manager.show_all_task()
    return flask.render_template('task_manager.html', task_list=task_list)


@view_server.route('/use_guide')
def use_guide():
    return flask.render_template('use_guide.html')


@view_server.route('/develop_document')
def develop_document():
    return flask.render_template('develop_ducument.html')


@view_server.route('/source_code')
def source_code():
    return flask.redirect('https://github.com/fkworld/my_graduation_project')


@view_server.route('/preview_3dmodel')
def preview_3dmodel():
    '''预览3D模型
    实际使用需要传入参数查询
    '''
    return flask.render_template('preview_3dmodel.html')

@view_server.route('/preview_result')
def preview_result():
    '''预览渲染结果
    实际使用需要传入参数查询
    '''
    return flask.render_template('preview_result.html')
