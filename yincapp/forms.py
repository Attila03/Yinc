from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        help_texts = {'username': None}



class ProfileForm(forms.ModelForm):

    class Meta:
        model=Profile
        exclude = ['user', ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 5})
        }


class ContactForm(forms.Form):

    name = forms.CharField()
    email = forms.EmailField(required=True)
    message = forms.CharField(
        widget = forms.Textarea()
    )