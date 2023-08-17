from django import forms
from django.core import validators
import email

class teacherRegistration(forms.Form):
    first_name = forms.CharField(label_suffix=' ')
    last_name = forms.CharField(label_suffix=' ')
    email = forms.EmailField(label_suffix=' ')
    password = forms.CharField(widget=forms.PasswordInput, label_suffix=' ')
    repassword = forms.CharField(widget=forms.PasswordInput, label_suffix=' ')
    Text_area = forms.CharField(widget=forms.Textarea, label_suffix=' ')
    file = forms.FileField(label_suffix=' ')

    def clean_repassword(self):
        password = self.cleaned_data.get('password')
        repassword = self.cleaned_data.get('repassword')

        if password and repassword and password != repassword:
            raise forms.ValidationError('Passwords do not match')

    def clean(self):
        cleaned_data = super().clean()
        # Other validation logic if needed

    # You can also have clean methods for other fields if needed

