from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Name"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email"}))
    message = forms.CharField(required=True, max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Message", 'rows': 5}))