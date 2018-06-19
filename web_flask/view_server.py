'''
针对server角色的蓝图
'''

import os

from flask import (Blueprint, redirect, render_template, request, session,
                   url_for)
from flask_socketio import emit

import server_start
import web_flask.formTask
from config import WEB_UPLOAD, WEB_UPLOAD_TEMP

TM = server_start.server.task_manager

view_server = Blueprint(
    'view_server', __name__, template_folder='templates')


@view_server.route('/')
def index():
    return render_template("index.html")


@view_server.route('/test')
def test():
    node_list = server_start.server.node_manager.show_all_node()
    node = node_list[0]
    a = url_for('static', filename='example.png')
    print(a)
    return render_template('preview_node.html', node=node)


@view_server.route('/node_manager')
def node_manager():
    node_list = server_start.server.node_manager.show_all_node()
    return render_template('node_manager.html', node_list=node_list)


@view_server.route('/task_manager')
def task_manager():
    task_list = TM.show_all_task()
    return render_template('task_manager.html', task_list=task_list)


@view_server.route('/task_manager/<task_id>/add_in_queue')
def task_manager_add_in_queue(task_id):
    TM.add_task_in_queue(task_id)
    return redirect(url_for("view_server.task_manager"))


@view_server.route('/task_queue_manager')
def task_queue_manager():
    queue = TM.show_all_queue()
    return render_template('queue_manager.html', queue=queue)


@view_server.route('/use_guide')
def use_guide():
    return render_template('use_guide.html')


@view_server.route('/develop_document')
def develop_document():
    return render_template('develop_ducument.html')


@view_server.route('/source_code')
def source_code():
    return redirect('https://github.com/fkworld/my_graduation_project')


@view_server.route('/preview_3dmodel')
def preview_3dmodel():
    '''预览3D模型
    实际使用需要传入参数查询
    '''
    return render_template('preview_3dmodel.html')


@view_server.route('/preview_result')
def preview_result():
    '''预览渲染结果
    实际使用需要传入参数查询
    '''
    return render_template('preview_result.html')


@view_server.route('/upload_task', methods=['GET', 'POST'])
def upload_task():
    """上传任务，包括任务信息和任务源文件

    Returns:
        render_template()
    """

    form = web_flask.formTask.TaskForm()
    if form.validate_on_submit():
        name = form.name.data
        info = form.info.data
        parameter = form.parameter.data
        TM.add_task(name, info, parameter)
        return redirect(url_for("view_server.task_manager"))
    return render_template('upload_task.html', form=form)


@view_server.route('/upload_task/upload_pieces', methods=['GET', 'POST'])
def upload_task_pieces():
    """文件的一个分片上传后调用

    Returns:
        redirect()
    """
    # 获取文件的唯一标识符
    task = request.form.get('task_id')
    # 获取该分片在所有分片中的序号
    chunk = request.form.get('chunk', 0)
    # 获取该分片的file
    upload_file = request.files['file']
    # 构造filename和save_path
    filename = '%s%s' % (task, chunk)
    save_path = WEB_UPLOAD_TEMP + task + '/'
    if(not os.path.exists(save_path)):
        os.makedirs(save_path)
    # 保存分片到本地
    upload_file.save(save_path + filename)
    return redirect(url_for("view_server.upload_task"))


@view_server.route('/upload_task/upload_success', methods=['GET', 'POST'])
def upload_task_success():
    """文件所有分片上传后调用

    Returns:
        redirect()
    """
    # 获取文件唯一标识符
    task = request.args.get('task_id')
    # 获取文件后缀名和文件类型
    ext = request.args.get('ext', '')
    upload_type = request.args.get('type')
    # 构建文件后缀名
    if len(ext) == 0 and upload_type:
        ext = upload_type.split('/')[1]
    ext = '' if len(ext) == 0 else '.%s' % ext
    # 起始分片
    chunk = 0
    with open(WEB_UPLOAD + '%s%s' % (task, ext), 'wb') as target_file:  # 创建新文件
        while True:
            try:
                filename = WEB_UPLOAD_TEMP + '%s/%s%d' % (task, task, chunk)
                source_file = open(filename, 'rb')  # 按序打开每个分片
                # 读取分片内容写入新文件
                target_file.write(source_file.read())
                source_file.close()
            except IOError:
                break
            # 分片序号+1
            chunk += 1
            # 删除该分片
            os.remove(filename)
        # 删除该分片所在的文件夹
        os.rmdir(WEB_UPLOAD_TEMP + '%s' % (task) + '/')
    return redirect(url_for("view_server.upload_task"))
