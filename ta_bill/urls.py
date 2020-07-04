from django.urls import path
from django.conf.urls import url
from .views import ta_create_view,ta_delete_view,ta_update_view,GeneratePDF
app_name = 'ta_bill'
urlpatterns = [
    path('pdfsec/<str:tit>/<str:emp>/',GeneratePDF,name='ta-pdf'),
    path('create/', ta_create_view, name='cert-list'),
    path('delete/<str:tit>/<str:emp>/',ta_delete_view,name='ta-delete'),
    path('update/<str:tit>/<str:emp>/',ta_update_view,name='ta-update'),

]