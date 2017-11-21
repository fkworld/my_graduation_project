from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from flask_uploads import UploadSet,IMAGES

file_images = UploadSet('photos', IMAGES)

class UploadForm(FlaskForm):
    file = FileField(validators=[FileRequired(u'Choose a file!')])
    # file = FileField(validators=[FileAllowed(file_images, u'Image Only!'), FileRequired(u'Choose a file!')])
    submit = SubmitField(u'Upload')
