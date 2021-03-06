from django.conf.urls import url
from yincapp.views import (Home, Register, Login, Logout, Contact, AddToCart, AddSubCart, RemoveFromCart, Order,
                            DisplayCart, EditProfile)


urlpatterns = [
    url(r'^$', Home.as_view(), name='homepage'),
    url(r'^Home/$', Home.as_view(), name='home'),
    url(r'Register/$', Register.as_view(), name='register'),
    url(r'Login/$', Login.as_view(), name='login'),
    url(r'Logout/$', Logout.as_view(), name='logout'),
    url(r'Contact/$', Contact.as_view(), name='contact'),
    url(r'AddToCart/$', AddToCart.as_view(), name='AddToCart'),
    url(r'AddSubCart/$', AddSubCart.as_view(), name='AddSubCart'),
    url(r'RemoveFromCart/$', RemoveFromCart.as_view(), name='RemoveFromCart'),
    url(r'Order/$', Order.as_view(), name='order'),
    url(r'DisplayCart/$', DisplayCart.as_view(), name='displaycart'),
    url(r'EditProfile/$', EditProfile.as_view(), name='editprofile'),
]