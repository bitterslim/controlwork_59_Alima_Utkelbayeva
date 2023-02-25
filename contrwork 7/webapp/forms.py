from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Guest


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('user', 'email', 'text')
        labels = {
            'user': 'User',
            'email': 'Email',
            'text': 'Text'
        }

    def clean_user(self):
        user = self.cleaned_data.get('user')
        if len(user) < 2:
            raise ValidationError('Your username is short')
        return user
