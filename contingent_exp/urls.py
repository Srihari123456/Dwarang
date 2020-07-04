from django.urls import path
from django.conf.urls import url
from .views import contingent_create_view,contingent_update_view,contingent_delete_view,GeneratePDF

app_name = 'contingent_exp'
urlpatterns = [
    path('pdfsec/<str:tit>/<str:emp>/',GeneratePDF,name='contingent-pdf'),
    path('create/', contingent_create_view, name='contingent-list'),
    path('delete/<str:tit>/<str:emp>/',contingent_delete_view,name='contingent-delete'),
    path('update/<str:tit>/<str:emp>/',contingent_update_view,name='contingent-update'),
]