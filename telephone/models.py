from django.db import models

# Create your models here.
class Telephone_Reim(models.Model):
    name        = models.CharField(max_length=120) #max_length required
    employee_id = models.CharField(max_length=20)  # max_length required
    designation = models.CharField(max_length=120) #max_length required
    amount      = models.DecimalField(decimal_places=2,max_digits=1000) 
    amount_words= models.TextField()
    department  = models.CharField(max_length=120) #max_length required
    month       = models.CharField(max_length=15)
    cred_month  = models.CharField(max_length=15)
    IFSC_Code   = models.CharField(max_length=12)
    Bank_name_branch = models.TextField()
    Bank_account_number = models.CharField(max_length=16)

