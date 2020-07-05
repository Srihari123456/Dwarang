from django.db import models

# Create your models here.
class Cert_A(models.Model):
    name        = models.CharField(max_length=120) #max_length required
    designation = models.CharField(max_length=120) #max_length required
    employee_id = models.CharField(max_length=20) #max_length required
    patient_name= models.CharField(max_length=120) #max_length required
    patient_age = models.IntegerField()
    employee_rel= models.CharField(max_length=120)
    doctor_address = models.TextField()
    disease     = models.CharField(max_length=120)
    dt1      = models.CharField(max_length=10)
    dt2      = models.CharField(max_length=10)
    
    Consult_dt1  = models.CharField(max_length=10)
    Consult_fee1 = models.DecimalField(decimal_places=2,max_digits=1000) 
    Injection_fee1      = models.DecimalField(decimal_places=2,max_digits=1000)
 
    Consult_dt2  = models.CharField(max_length=10,blank=True,null=True)
    Consult_fee2 = models.DecimalField(decimal_places=2,max_digits=1000,blank=True,null=True)
    Injection_fee2     = models.DecimalField(decimal_places=2,max_digits=1000,blank=True,null=True)
 
    Med_name1      = models.CharField(max_length=120) #max_length required
    Quantity1       = models.IntegerField()
    Price1     = models.DecimalField(decimal_places=2,max_digits=1000)
    Med_CashMemoNo1 = models.CharField(max_length=120) #max_length required
    
    Med_name2      = models.CharField(max_length=120,blank=True,null=True) #max_length required
    Quantity2       = models.IntegerField(blank=True,null=True)
    Price2     = models.DecimalField(decimal_places=2,max_digits=1000,blank=True,null=True)
    Med_CashMemoNo2 = models.CharField(max_length=120,blank=True,null=True) #max_length required
   
    DiagTest_name1   = models.CharField(max_length=120) #max_length required
    DiagTest_center1 = models.CharField(max_length=120) #max_length required
    Diagnostic_Test_price1  = models.DecimalField(decimal_places=2,max_digits=1000)
    
    
    DiagTest_name2   = models.CharField(max_length=120,blank=True,null=True) #max_length required
    DiagTest_center2 = models.CharField(max_length=120,blank=True,null=True) #max_length required
    Diagnostic_Test_price2  = models.DecimalField(decimal_places=2,max_digits=1000,blank=True,null=True)
   
    RefDoc =  models.CharField(max_length=120) #max_length required
    station = models.CharField(max_length=120) #max_length required
    #Total_amount      = models.DecimalField(decimal_places=2,max_digits=1000)
     