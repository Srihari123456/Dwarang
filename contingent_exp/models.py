from django.db import models

# Create your models here.
class Contingent_exp(models.Model):
    name = models.CharField(max_length=120)  # max_length required
    employee_id = models.CharField(max_length=120)  # max_length required

    dt1      = models.CharField(max_length=10)
    description1 = models.TextField() 
    amount1      = models.DecimalField(decimal_places=2,max_digits=1000) 
    
    dt2      = models.CharField(max_length=10,blank=True,null=True)
    description2 = models.TextField(blank=True,null=True) 
    amount2      = models.DecimalField(decimal_places=2,max_digits=1000,blank=True,null=True,default=0) 
    
    dt3      = models.CharField(max_length=10,blank=True,null=True)
    description3 = models.TextField(blank=True,null=True) 
    amount3      = models.DecimalField(decimal_places=2,max_digits=1000,blank=True,null=True,default=0) 
    
    #totamount = amount1+amount2+amount3
    Total_amount      = models.DecimalField(decimal_places=2,max_digits=1000)
    
    amount_words= models.TextField()
    station = models.CharField(max_length=120) #max_length required
    address     = models.TextField()
    IFSC_Code   = models.CharField(max_length=12)
    Bank_name_branch = models.TextField()
    Bank_account_number = models.CharField(max_length=16)
    
