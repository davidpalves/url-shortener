from django import forms
from shorten.models import Encurtador
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EncurtadorForm(forms.ModelForm):
    url_redirect = forms.CharField(label='URL to be shortened', required=True)

    class Meta:
        model = Encurtador
        fields = ('url_redirect',)



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )