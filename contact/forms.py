from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):

    class Meta(object):
        model = ContactMessage
        exclude = ('date_readed', 'date_')