from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


# class UserCreateForm(UserCreationForm):
#     class Meta:
#         fields = ("username", "email", "password1", "password2")
#         model = get_user_model()
#
#     def __init__(self, *args, **kwargs):
#         super(UserCreateForm, self).__init__()
#         self.fields["username"].label = "Display name"
#         self.fields["email"].label = "Email address"

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
