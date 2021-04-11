# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages ,auth

def login(request):
    #TODO add user login or logout
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username ,password=password )

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now loged in')
            return redirect("home")
        else:
            messages.error(request, "You'r username or passwerd is wrong")
            return redirect("accounts_login")
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        messages.success(request, 'You are now loged out')
        return redirect('accounts_login')
    else:
        messages.error(request, "Something went wrong!!!")
        return redirect('accounts_login')