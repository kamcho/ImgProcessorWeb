from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    img = forms.ImageField()