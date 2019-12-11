from django import forms
from .models import ContactUs

class ContactUs(forms.ModelForm):
    name=forms.CharField(label="name")
    email=forms.EmailField(label="email")
    subject=forms.CharField(max_length=100, label="subject")
    message=forms.CharField(widget=forms.Textarea, label="message")

    class Meta:
        model=ContactUs
        fields=['name', 'email', 'subject', 'message']