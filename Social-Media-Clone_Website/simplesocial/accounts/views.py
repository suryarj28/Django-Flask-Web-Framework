from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from .models import User, Users


# Create your views here.


class SignUp(CreateView):
    form_class = forms.UserForm
    model = Users
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

    def form_valid(self, form):
        return super(SignUp, self).form_valid(form)

    def form_invalid(self, form):
        return super(SignUp, self).form_invalid(form)

