from django import forms

from .models import User

class SearchUser(forms.Form):
    name = forms.CharField(
        label='Username',
        error_messages={'required': 'Introdueix un usuari'},
    )
