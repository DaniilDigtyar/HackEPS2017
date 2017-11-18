from django import forms

class SearchUser(forms.Form):
    name = forms.CharField(
        label='Username',
        error_messages={'required': 'Introdueix un usuari'},
    )
