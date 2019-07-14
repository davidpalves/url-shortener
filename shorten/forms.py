from django import forms
from shorten.models import Encurtador


class EncurtadorForm(forms.ModelForm):
    url_redirect = forms.CharField(label='URL to be shortened')

    class Meta:
        model = Encurtador
        fields = ('url_redirect',)
