from django.urls import path
from django.conf.urls import url
from .views import dashboard_view,actions_form_view


app_name = 'dashboard'
urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('actions/<str:pg>', actions_form_view, name='actions'),
]