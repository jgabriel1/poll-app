from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, FieldList, TextField
from wtforms.validators import Required


class CreateForm(FlaskForm):
    question = TextField(
        label='Question: ',
        id='poll-question',
        validators=[Required()],
        render_kw={'class_': 'form-control'}
    )

    allow_multiple = BooleanField(
        label='Allow more than one answer.',
        id='allow-multiple',
        render_kw={'class_': 'form-check-input'}
    )

    options = FieldList(
        min_entries=2,
        unbound_field=TextField(
            render_kw={'class_': 'form-control poll-option'}
        ),
    )


class PollForm(FlaskForm):
    @classmethod
    def from_dict(cls, poll: dict):
        return cls()
