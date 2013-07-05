from django.views.generic import CreateView
from .forms import ContactForm


class ContactView(CreateView):
    form_class = ContactForm
    success_url =  '/'