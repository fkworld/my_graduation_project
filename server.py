from flask import Flask, render_template, send_file, send_from_directory, make_response, request
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

from serverDB import ServerDB

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '42'
app.config['DEBUG'] = True
# 配置文件上传的路径
app.config['UPLOADED_PHOTOS_DEST'] = 'upload'
# 配置文件的限制类型
app.config['UPLOADED_PHOTO_ALLOW'] = IMAGES

# 实例化UploadSet
from form import file_images
# 将 app 的 config 配置注册到 UploadSet 实例 file_images （这是人说的话吗）
configure_uploads(app, file_images)
# 限制上传文件的大小
patch_request_class(app, 32 * 1024 * 1024) # 32MB


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
        from form import file_images
        file.name = file_images.save(form.file.data)
        file.sourcefile_url = file_images.url(file.name)
        file.sourcefile_path = file_images.path(file.name)
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


@app.route('/needtask')
def needtask():
    print("node is asking for task.")
    response = make_response(send_file("README.md"))
    response.headers["Content-Disposition"] = "attachment; filename=README.md;"
    return response

@app.route('/3dmodel')
def _3dmodel():
    file = open("out/test.js", 'r')
    try:
        text = file.read()
    finally:
        file.close()
    return render_template("3dmodel.html", file_js = text)

if __name__ == '__main__':
    app.run()
