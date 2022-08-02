from django import forms
from .models import Contact



class ContactForm(forms.ModelForm):
    """form for visitors to contact us"""

    class Meta:
        model = Contact
        fields = ['name', 'email']
        labels = {'name': 'Name','email' : 'E-mail'}

