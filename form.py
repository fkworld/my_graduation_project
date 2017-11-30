from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from flask_uploads import UploadSet, IMAGES


class UploadForm(FlaskForm):
    file = FileField(u'文件上传', validators=[FileRequired(u'需要选择一个渲染文件')])
    # file = FileField(validators=[FileAllowed(file_images, u'Image Only!'), FileRequired(u'Choose a file!')])
    submit = SubmitField(u'上传')
