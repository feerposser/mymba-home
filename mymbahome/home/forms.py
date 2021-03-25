from django import forms

from .models import ModelContact


class FormContact(forms.ModelForm):
    class Meta:
        model = ModelContact
        fields = ("name", "email", "subject", "message",)
