from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    '''任务提交表单
    '''
    name = StringField(u'任务名称', validators=[DataRequired(u'请输入任务名称')])
    info = StringField(u'任务描述')
    parameter = StringField(u'任务执行参数')
    submit = SubmitField(u'提交任务')
