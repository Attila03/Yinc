from django.shortcuts import render, HttpResponse, reverse, redirect
from django.contrib.auth import login, logout, authenticate
from django.views import View

from .models import Product, Cart
from .forms import UserForm, ProfileForm, ContactForm, UserLoginForm
from .Cart import cart_add, cart_remove, cart_sub, sessioncart_to_dbcart

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

        if not request.session.get("sessioncart_created"):
            request.session["cart"] = {}
            request.session["total"] = 0
            request.session["sessioncart_created"] = True
        # request.session.set_expiry(0)
        # print(request.session.get_expiry_age())
        # print(request.session.get_expire_at_browser_close())
        return render(request, 'yincapp/Home.html', context=context)


class AddToCart(View):

    def get(self, request, *args, **kwargs):
        cart_add(request, request.session["cart"], request.GET['product_id'])
        print(request.session["cart"])
        return HttpResponse()


class AddSubCart(View):

    def get(self, request, *args, **kwargs):
        if request.GET['operation'] == "add":
            cart_add(request, request.session["cart"], request.GET['product_id'])
        else:
            cart_sub(request, request.session["cart"], request.GET['product_id'])
        return HttpResponse()


class RemoveFromCart(View):

    def get(self, request, *args, **kwargs):
        cart_remove(request, request.session["cart"], request.GET['product_id'])
        return HttpResponse()


class DisplayCart(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'yincapp/DisplayCart.html', )




class Order(View):

    def get(self, request, *args, **kwargs):
        customer = request.user
        if not request.session.get('dbcart_created'):
            new_cart = Cart(customer=customer, total=request.session["total"])
            new_cart.save()
            print(new_cart.id)
            sessioncart_to_dbcart(request, request.session["cart"], new_cart)
            return render(request, 'yincapp/Order.html', )


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
            if not request.session.get("sessioncart_created"):
                request.session["cart"] = {}
                request.session["total"] = 0
                request.session["sessioncart_created"] = True
            return redirect(reverse('home'))
        context = {
            'UserForm': user_form,
            'ProfileForm': profile_form
        }
        return render(request, 'yincapp/Register.html', context=context)


class Login(View):

    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'yincapp/Login.html', context=context)

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user=user)
            if not request.session.get("sessioncart_created"):
                request.session["cart"] = {}
                request.session["total"] = 0
                request.session["sessioncart_created"] = True
            return redirect(reverse('home'))
        return render(request, 'yincapp/Login.html', context=context)


class Logout(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('home'))


class Contact(View):

    def get(self, request, *args, **kwargs):
        context = {
            'ContactForm': ContactForm()
        }
        return render(request, 'yincapp/Contact.html', context=context)



