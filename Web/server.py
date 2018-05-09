from flask import Flask, render_template, send_file, send_from_directory, make_response, request, jsonify
from flask_uploads import UploadSet, configure_uploads, ALL, patch_request_class

from serverDB import ServerDB
import os
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = '42'
app.config['DEBUG'] = True

# 实例化UploadSet
files = UploadSet('files', ALL)
# 配置文件上传的路径
app.config['UPLOADS_DEFAULT_DEST'] = 'upload'
# 将 app 的 config 配置注册到 UploadSet 实例 _uploads （这是人说的话吗）
configure_uploads(app, files)
# 限制上传文件的大小:1024MB
patch_request_class(app, 1024 * 1024 * 1024)


server_db = ServerDB(app)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    from form import UploadForm
    form = UploadForm()
    from Task import MainTask
    file = MainTask()
    if form.validate_on_submit():
        _filename = form.file.data.filename  # 获取上传文件的文件名
        _filetype = '.' + _filename.split('.')[-1]  # 获取上传文件的文件类型
        file.mname = _filename
        # 根据文件名和当前时间计算哈希值作为文件的存储名
        _file_savename = str(hash(_filename + str(time.time()))) + _filetype
        file.name = files.save(form.file.data, name=_file_savename)
        file.sourcefile_url = files.url(file.name)
        file.sourcefile_path = files.path(file.name)
        file.add_to_db()
        success = True
    else:
        file_url = None
        success = False
    return render_template('upload.html', form=form, file_url=file.sourcefile_url, success=success)


@app.route('/manage')
def manage_file():
    from Task import MainTask
    file = MainTask()
    file_list = file.searh_all()
    return render_template('manage.html', file_list=file_list)


@app.route('/register')
def register():
    print("node is success register.")
    print(request)
    return "sucecess"


@app.route('/ask_task')
def ask_task():
    # 节点请求任务，用json作为传递任务参数的媒介
    # 包含：任务id，任务资源下载地址，任务结果上传地址，任务目标节点
    from TaskQueue import TaskQueue
    print("node is asking for task...")
    test = TaskQueue()
    # 这里需要写test=，不明原因
    test = test.get()
    _response = jsonify(test.to_json_dict())
    return _response


@app.route('/download_sourcefile/<sourcefile_filename>')
def download_sourcefile(sourcefile_filename):
    print("node is download sourcefile...")
    filename = "README.md"
    response = make_response(send_file(filename))
    response.headers["Content-Disposition"] = "attachment"
    # 这里添加一个filetype项目来标识文件的类型
    response.headers['_filetype'] = '.' + \
        filename.split('.')[-1]  # 用-1来获取最后一个元素
    return response


@app.route('/3dmodel')
def _3dmodel():
    file = open("out/test.js", 'r')
    try:
        text = file.read()
    finally:
        file.close()
    return render_template("3dmodel.html", file_js=text)


if __name__ == '__main__':
    app.run()
