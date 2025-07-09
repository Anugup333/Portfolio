from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phonenumber', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10-digit number'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'How can i help you?', 'rows': 4}),
        }
