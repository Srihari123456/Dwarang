from django.db import models

# Create your models here.
class Reimbursement(models.Model):
    name        = models.CharField(max_length=120) #max_length required
    employee_id = models.CharField(max_length=120)  # max_length required
    department  = models.CharField(max_length=120) #max_length required
    net_claimed   = models.DecimalField(decimal_places=2,max_digits=1000) 
 
    dt1      = models.CharField(max_length=10)
    cashmemo1 = models.TextField() 
    firmname1 = models.TextField() 
    purpose1 = models.TextField() 
    amount1      = models.DecimalField(decimal_places=2,max_digits=1000) 
    
    dt2      = models.CharField(max_length=10,blank=True,null=True)
    cashmemo2 = models.TextField(blank=True,null=True) 
    firmname2 = models.TextField(blank=True,null=True) 
    purpose2 = models.TextField(blank=True,null=True) 
    amount2      = models.DecimalField(decimal_places=2,max_digits=1000,blank=True,null=True) 

    dt3      = models.CharField(max_length=10,blank=True,null=True)
    cashmemo3 = models.TextField(blank=True,null=True) 
    firmname3 = models.TextField(blank=True,null=True) 
    purpose3 = models.TextField(blank=True,null=True) 
    amount3      = models.DecimalField(decimal_places=2,max_digits=1000,blank=True,null=True) 

    dt4      = models.CharField(max_length=10,blank=True,null=True)
    cashmemo4 = models.TextField(blank=True,null=True) 
    firmname4 = models.TextField(blank=True,null=True) 
    purpose4 = models.TextField(blank=True,null=True) 
    amount4      = models.DecimalField(decimal_places=2,max_digits=1000,blank=True,null=True) 

    dt5      = models.CharField(max_length=10,blank=True,null=True)
    cashmemo5 = models.TextField(blank=True,null=True) 
    firmname5 = models.TextField(blank=True,null=True) 
    purpose5 = models.TextField(blank=True,null=True) 
    amount5      = models.DecimalField(decimal_places=2,max_digits=1000,blank=True,null=True) 
     
    #totamount = amount1+amount2+amount3
    Total_amount      = models.DecimalField(decimal_places=2,max_digits=1000)
    amount_words= models.TextField()
    
    IFSC_Code   = models.CharField(max_length=12)
    Bank_name_branch = models.TextField()
    Bank_account_number = models.CharField(max_length=16)
    
