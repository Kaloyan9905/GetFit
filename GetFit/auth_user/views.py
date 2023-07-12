from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model

from GetFit.auth_user.forms import UserCreateForm

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'login-form.html'


class SignUpView(views.CreateView):
    template_name = 'register-form.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('main page')
