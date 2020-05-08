from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, FieldList, TextField
from wtforms.validators import Required


class CreateForm(FlaskForm):
    query = TextField(
        label='Question: ',
        id='poll-question',
        validators=[Required()],
        render_kw={'class_': 'form-control'}
    )

    options = FieldList(
        min_entries=3,
        unbound_field=TextField(
            render_kw={'class_': 'form-control poll-option'}
        ),
    )

    multiple_answers = BooleanField(
        label='Allow more than one answer.',
        id='allow-multiple-checkbox',
        render_kw={'class_': 'form-check-input'}
    )


class PollForm(FlaskForm):
    @classmethod
    def from_dict(cls, poll: dict):
        return cls()
