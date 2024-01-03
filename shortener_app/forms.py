from django import forms
from shortener_app.models import Url

class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['full_url']
        submitted_url = forms.CharField(label="Enter URL", max_length=200)