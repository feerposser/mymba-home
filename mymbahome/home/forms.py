from django import forms

from .models import ModelContact, ModelNewsletterAssign


class FormContact(forms.ModelForm):
    class Meta:
        model = ModelContact
        fields = ("name", "email", "office",)


class FormNewsletterAssign(forms.ModelForm):
    class Meta:
        model = ModelNewsletterAssign
        fields = ("email",)
