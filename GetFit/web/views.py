from django import forms
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views.generic import View

from GetFit.web.forms import LoginForm


class IndexView(View):
    def get(self, request):
        return render(request, 'start-page.html')


def login(request):
    form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'login-form.html', context)
