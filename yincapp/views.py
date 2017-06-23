from django.shortcuts import render, HttpResponse, reverse, redirect
from django.contrib.auth import login, logout, authenticate
from django.views import View

from .models import Product
from .forms import UserForm, ProfileForm, ContactForm

# Create your views here.

class Home(View):

    def get(self, request, *args, **kwargs):
        Books = Product.objects.filter(category='BK')
        Watches = Product.objects.filter(category='WH')
        Food = Product.objects.filter(category='FD')
        Games = Product.objects.filter(category='GM')
        context = {
            'Books': Books,
            'Games': Games,
            'Food': Food,
            'Watches': Watches
        }
        return render(request, 'yincapp/Home.html', context=context)


class Register(View):

    def get(self, request, *args, **kwargs):
        context = {
            'UserForm': UserForm(),
            'ProfileForm': ProfileForm()
        }
        return render(request, 'yincapp/Register.html', context=context)

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            ProfileForm(request.POST, instance=new_user.profile).save()
            login(request, new_user)
            return redirect(reverse('home'))
        context = {
            'UserForm': user_form,
            'ProfileForm': profile_form
        }
        return render(request, 'yincapp/Register.html', context=context)



class Contact(View):

    def get(self, request, *args, **kwargs):
        context = {
            'ContactForm': ContactForm()
        }
        return render(request, 'yincapp/Contact.html', context=context)