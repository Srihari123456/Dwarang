from django.urls import path
from django.conf.urls import url
from .views import travel_create_view,travel_update_view,travel_delete_view,GeneratePDF

app_name = 'travel_adv'
urlpatterns = [
    path('pdfsec/<str:tit>/<str:emp>/',GeneratePDF,name='travel-pdf'),
    path('create/', travel_create_view, name='travel-list'),
    path('delete/<str:tit>/<str:emp>/',travel_delete_view,name='travel-delete'),
    path('update/<str:tit>/<str:emp>/',travel_update_view,name='travel-update'),
]