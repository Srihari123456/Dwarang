from django.urls import path
from django.conf.urls import url
from .views import reimbursement_create_view,reimbursement_update_view,reimbursement_delete_view,GeneratePDF

app_name = 'reimbursement'
urlpatterns = [
    path('pdfsec/<str:tit>/<str:emp>/',GeneratePDF,name='reimbursement-pdf'),
    path('create/', reimbursement_create_view, name='reimbursement-list'),
    path('delete/<str:tit>/<str:emp>/',reimbursement_delete_view,name='reimbursement-delete'),
    path('update/<str:tit>/<str:emp>/',reimbursement_update_view,name='reimbursement-update'),
]