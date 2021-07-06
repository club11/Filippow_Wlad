from django import forms
from django.contrib.auth import password_validation
#from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm

#from django.contrib.auth.validators import UnicodeUsernameValidator

from django.db import models
from django.core.mail import send_mail

from django.contrib.auth import get_user_model
User = get_user_model()  

username_validator = UnicodeUsernameValidator()
is_user_unique = UnicodeUsernameValidator()

class RegisterForm(forms.Form):
    username =forms.CharField(max_length="150", required=True, label="Username", validators=[username_validator, is_user_unique])       #допилить проверку на уникального пользователя
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )
    tel =forms.CharField(max_length='15', required=True, label="номер телефона", help_text='+375290000000')
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                'Пароли не совпадают',
                code='password_mismatch',
            )
        try:
            validate_password(password2, User)
        except ValidationError as error:
            self.add_error('password2', error)
        return password2

    def clean_tel(self):
        tel_plus = self.cleaned_data.get("tel")[0]
        tel_numb = self.cleaned_data.get("tel")[1:] 
        tel = self.cleaned_data.get("tel")
        if not tel_numb.isdigit():
            raise ValidationError(
                'не цифры',
                code='password_mismatch',
            )
        if tel_plus !='+':
            raise ValidationError(
                'не телефонный формат + ...',
                code='password_mismatch',
            )
        return tel    


    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)    



