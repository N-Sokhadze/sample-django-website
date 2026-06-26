from django import forms
from email_validator import validate_email, EmailNotValidError

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Name"}))
    
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email"}))
    
    # _______email validator________

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email, check_deliverability=True)
        except EmailNotValidError:
            raise forms.ValidationError('Please enter a valid email address.')
        return email
    # _______________________________
    
    message = forms.CharField(required=True, max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Message", 'rows': 5}))