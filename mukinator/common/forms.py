from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from common.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    nickname = forms.CharField(max_length=10)
    region = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "nickname", "region")


class UserUpdateForm(UserChangeForm):
    email = forms.EmailField(label="이메일")
    nickname = forms.CharField(max_length=10)
    region = forms.CharField(max_length=10)

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "nickname", "region")