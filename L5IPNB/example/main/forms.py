from django.forms import Form, fields, widgets
from django.core.exceptions import ValidationError


class ExampleForm(Form):

    message = fields.CharField(
        label='Сообщение',
        required=True, max_length=128,
        widget=widgets.Textarea(
            attrs={'class': 'message'}
        )
    )

    def clean_message(self):
        value = self.cleaned_data.get('message')
        if not value.startswith('Привет,'):
            raise ValidationError('Сообщение должно начинаться с приветствия!')
        return value
