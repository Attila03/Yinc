from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile

class UserForm(forms.ModelForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        help_texts = {'username': None}


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['user',]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 5})
        }


class EditProfileForm(forms.ModelForm):

    class Meta:
        model=Profile
        exclude = ['user',]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 5})
        }



class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.filter(username=username)
        if not user:
            raise forms.ValidationError('Username does not exist')
        else:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError('Incorrect password for the username.')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class ContactForm(forms.Form):

    name = forms.CharField()
    email = forms.EmailField(required=True)
    message = forms.CharField(
        widget=forms.Textarea()
    )