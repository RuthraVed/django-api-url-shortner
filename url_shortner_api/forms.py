from django import forms

from url_shortner_api.models import Link


class ShortenerForm(forms.ModelForm):

    original_link = forms.URLField(widget=forms.URLInput(attrs={"class": "form-control form-control-lg", "placeholder": "Give a URL to shorten"}))

    class Meta:
        model = Link
        fields = ("original_link",)
