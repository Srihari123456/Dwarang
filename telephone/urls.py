from django.urls import path
from django.conf.urls import url
from .views import telephone_create_view,telephone_update_view,telephone_delete_view,GeneratePDF
app_name = 'telephone'
urlpatterns = [
    path('pdfsec/<str:tit>/<str:emp>/',GeneratePDF,name='telephone-pdf'),
    path('create/', telephone_create_view, name='telephone-create'),
    path('delete/<str:tit>/<str:emp>/',telephone_delete_view,name='telephone-delete'),
    path('update/<str:tit>/<str:emp>/',telephone_update_view,name='telephone-update'),
]