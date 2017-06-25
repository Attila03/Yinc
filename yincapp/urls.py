from django.conf.urls import url
from yincapp.views import Home, Register, Login, Logout, Contact, AddToCart


urlpatterns = [
    url(r'^Home/$', Home.as_view(), name='home'),
    url(r'Register/$', Register.as_view(), name='register'),
    url(r'Login/$', Login.as_view(), name='login'),
    url(r'Logout/$', Logout.as_view(), name='logout'),
    url(r'Contact/$', Contact.as_view(), name='contact'),
    url(r'AddToCart/$', AddToCart.as_view(), name='AddToCart'),
]