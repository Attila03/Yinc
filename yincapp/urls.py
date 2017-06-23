from django.conf.urls import url
from yincapp.views import Home, Register, Contact


urlpatterns = [
    url(r'^Home/$', Home.as_view(), name='home'),
    url(r'Register/$', Register.as_view(), name='register'),
    url(r'Contact/$', Contact.as_view(), name='contact')
]