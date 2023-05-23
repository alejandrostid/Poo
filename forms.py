from wtforms import *
from wtforms import StringField
from wtforms.fields import EmailField


class sendDate(Form):
    usuario = StringField('usuario')
    email = EmailField('email')