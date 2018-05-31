'''
针对server角色的蓝图
'''

from flask import Blueprint, render_template, url_for, request, redirect, session
from flask_socketio import emit
import os

import server_start
import web_flask.formTask

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
    task_list = server_start.server.task_manager.show_all_task()
    return render_template('task_manager.html', task_list=task_list)


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
    form = web_flask.formTask.TaskForm()
    print("获取文件的唯一标识符")
    print(request)
    return render_template('upload_task.html', form=form)


@view_server.route('/upload_task/upload_pieces', methods=['GET', 'POST'])
def upload_task_pieces():
    '''文件的一个分片上传后调用
    '''
    print("upload_pieces")
    task = request.form.get('task_id')  # 获取文件的唯一标识符
    chunk = request.form.get('chunk', 0)  # 获取该分片在所有分片中的序号
    filename = '%s%s' % (task, chunk)  # 构造该分片的唯一标识符

    upload_file = request.files['file']
    upload_file.save('upload/'+filename)  # 保存分片到本地
    return redirect(url_for("view_server.upload_task"))


@view_server.route('/upload_task/upload_success', methods=['GET', 'POST'])
def upload_task_success():
    '''文件所有分片上传后调用
    '''
    print("upload_success")
    task = request.args.get('task_id')
    ext = request.args.get('ext', '')
    upload_type = request.args.get('type')
    print(upload_type, ext)
    if len(ext) == 0 and upload_type:
        ext = upload_type.split('/')[1]
    print(ext)
    ext = '' if len(ext) == 0 else '.%s' % ext      # 构建文件后缀名
    chunk = 0
    with open('upload/%s%s' % ("newfilename", ext), 'wb') as target_file:  # 创建新文件
        while True:
            try:
                filename = 'upload/%s%d' % (task, chunk)
                source_file = open(filename, 'rb')  # 按序打开每个分片
                # 读取分片内容写入新文件
                target_file.write(source_file.read())
                source_file.close()
            except IOError:
                break
            chunk += 1
            os.remove(filename)                     # 删除该分片，节约空间
    return redirect(url_for("view_server.upload_task"))
