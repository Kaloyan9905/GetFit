from django import forms

from GetFit.web.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'input100',
                    'placeholder': 'Email',
                    'style': 'font-family: "Poppins-Regular";'
                }
            ),

            'password': forms.PasswordInput(
                attrs={
                    'class': 'input100',
                    'placeholder': 'Password'
                }
            ),
        }
