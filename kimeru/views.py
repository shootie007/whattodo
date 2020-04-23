# from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from . import forms


class SigninView(LoginView):
    form_class = forms.SigninForm
    template_name = "kimeru/signin.html"


class SignoutView(LoginRequiredMixin, LogoutView):
    template_name = "kimeru/signout.html"


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "kimeru/userCreate.html"
    success_url = reverse_lazy('signin')


class IndexView(TemplateView):
    template_name = "kimeru/index.html"
