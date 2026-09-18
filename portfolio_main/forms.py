from django.contrib.auth.models import user
from django.contrib.auth.forms import UserCreationForm


class registrationForm(UserCreationForm):


class meta:
    model = User
    fields = ('email', 'username', 'password1', 'password2')
