from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

UserModel = get_user_model()


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['username', 'email']
        field_classes = {
            'username': UsernameField
        }

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'id': 'form3Example1c',
                    'class': 'form-control',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'id': 'form3Example3c',
                    'class': 'form-control',
                }
            ),
            # 'password1': forms.PasswordInput(
            #     attrs={
            #         'id': 'form3Example4c',
            #         'class': 'form-control',
            #         'type': 'password',
            #     }
            # ),
            # 'password2': forms.PasswordInput(
            #     attrs={
            #         'id': 'form3Example4cd',
            #         'class': 'form-control',
            #         'type': 'password',
            #     }
            # ),
        }
