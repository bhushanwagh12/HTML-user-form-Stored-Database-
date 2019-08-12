from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(max_length=50)
    salary=forms.FloatField()
    email=forms.EmailField(max_length=100)
    city=forms.CharField(max_length=40)

