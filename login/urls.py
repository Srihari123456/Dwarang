from django.urls import path
from django.conf.urls import url
from .views import logout_view,login_view,signup_view

app_name = 'login'
urlpatterns = [
    path('',signup_view, name='registration-form'),
    path('create_acc/',login_view, name='loginpage'),
    path('logout/',logout_view,name='logout')
]