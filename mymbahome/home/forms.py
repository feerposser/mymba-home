from django import forms

from .models import ModelContact, ModelNewsletterAssign


class FormContact(forms.ModelForm):
    class Meta:
        model = ModelContact
        fields = ("name", "email", "subject", "message",)


class FormNewsletterAssign(forms.ModelForm):
    class Meta:
        model = ModelNewsletterAssign
        fields = ("email",)
