from django import forms

class SearchUser(forms.Form):
    name1 = forms.CharField(
        label='Username1',
        error_messages={'required': 'Introdueix un usuari'},
        widget=forms.TextInput(
        	attrs={
        		'class':'form-control form-control-lg',
        		'placeholder':'Nicolas Tesla...'}
        )
    )
    name2 = forms.CharField(
        label='Username2',
        error_messages={'required': 'Introdueix un usuari'},
         widget=forms.TextInput(
        	attrs={
        		'class':'form-control form-control-lg',
        		'placeholder':'Thomas Edison...'}
        )
    )
