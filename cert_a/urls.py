from django.urls import path
from django.conf.urls import url
from .views import cert_create_view,cert_update_view,cert_delete_view,GeneratePDF

app_name = 'cert_a'
urlpatterns = [
    path('pdfsec/<str:tit>/<str:emp>/',GeneratePDF,name='cert-pdf'),
    path('create/', cert_create_view, name='cert-list'),
    path('delete/<str:tit>/<str:emp>/',cert_delete_view,name='cert-delete'),
    path('update/<str:tit>/<str:emp>/',cert_update_view,name='cert-update'),
]