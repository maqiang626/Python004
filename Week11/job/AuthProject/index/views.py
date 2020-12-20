import this
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django import forms
from .form import LoginForm


def login2(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                zen = "".join([this.d.get(c, c) for c in this.s])
                return render(request, 'main.html', {'welcome': zen})
            else:
                return render(request, 'index.html', {'form': login_form, 'error_msg': '用户或密码出错'})

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'index.html', {'form': login_form})
