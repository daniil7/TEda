import re

from django import forms
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_email(value):
    """
    Validate that user typed a correct email address
    """
    if not re.match(r"^.*@(study.utmn.ru|utmn.ru)$", value):
        raise ValidationError(
            f"{value} неподходящий адрес электронной почты",
            params={"value": value},
        )

class UserCreationForm(DjangoUserCreationForm):
    email = forms.EmailField(required=True, validators=[validate_email])
    class Meta(DjangoUserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
