from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input is-medium'}),
    )
    password = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input is-large'}),
    )
