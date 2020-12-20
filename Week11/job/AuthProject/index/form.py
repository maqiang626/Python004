from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': 'User'}), min_length=1, label="用户名")
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", 'placeholder': 'Password'}), min_length=9, label="密码")
