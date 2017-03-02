from django.conf.urls import url
from . import views  # the views.py file in 'accounts' app

app_name = 'accounts'  # use this variable to organise the HTML files ex. {% urls 'accouns:login' %}

urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.loginView, name='login'),
]
