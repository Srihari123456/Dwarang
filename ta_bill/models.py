from django.db import models
CHOICES = (
    ('Air','Air'),
    ('Rail', 'Rail'),
    ('Road','Road'),
    ('-','-'),
    
)
class TA_Bill(models.Model):
    name        = models.CharField(max_length=120) #max_length required
    employee_id = models.CharField(max_length=20) #max_length required
    designation = models.CharField(max_length=120) #max_length required
    department = models.CharField(max_length=120) #max_length required
    institute = models.CharField(max_length=120) #max_length required
    basicpay = models.DecimalField(decimal_places=2,max_digits=1000) 
    institute_acc_no = models.CharField(max_length=120) #max_length required
    purpose = models.TextField()
    
    dep_station_1 = models.CharField(max_length=120) #max_length required
    dep_date_1 = models.CharField(max_length=10)
    arr_station_1 = models.CharField(max_length=120) #max_length required
    arr_date_1 = models.CharField(max_length=10)
    mode_of_journey_1 = models.CharField(max_length=60, choices=CHOICES, default='-')
    ticket_no_1 = models.CharField(max_length=120) #max_length required
    fare_1 =  models.DecimalField(decimal_places=2,max_digits=1000) 
    
    dep_station_2 = models.CharField(max_length=120,blank=True,null=True) #max_length required
    dep_date_2 = models.CharField(max_length=10,blank=True,null=True)
    arr_station_2 = models.CharField(max_length=120,blank=True,null=True) #max_length required
    arr_date_2 = models.CharField(max_length=10,blank=True,null=True)
    mode_of_journey_2 = models.CharField(max_length=60, choices=CHOICES, default='-',)
    ticket_no_2 = models.CharField(max_length=120,blank=True,null=True) #max_length required
    fare_2 =  models.DecimalField(decimal_places=2,max_digits=1000,blank=True,null=True) 

    dep_station_3 = models.CharField(max_length=120,blank=True,null=True) #max_length required
    dep_date_3 = models.CharField(max_length=10,blank=True,null=True)
    arr_station_3 = models.CharField(max_length=120,blank=True,null=True) #max_length required
    arr_date_3 = models.CharField(max_length=10,blank=True,null=True)
    mode_of_journey_3 = models.CharField(max_length=60, choices=CHOICES, default='-')
    ticket_no_3 = models.CharField(max_length=120,blank=True,null=True) #max_length required 
    fare_3 =  models.DecimalField(decimal_places=2,max_digits=1000,blank=True,null=True) 

    #Total_amount_A  = models.DecimalField(decimal_places=2,max_digits=1000)
    
    other_exp_item_1 = models.CharField(max_length=120) #max_length required
    other_exp_amount_1 =  models.DecimalField(decimal_places=2,max_digits=1000) 
    other_exp_billdetails_1 = models.CharField(max_length=120) #max_length required
    
    
    other_exp_item_2 = models.CharField(max_length=120,blank=True,null=True) #max_length required
    other_exp_amount_2 =  models.DecimalField(decimal_places=2,max_digits=1000,blank=True,null=True) 
    other_exp_billdetails_2 = models.CharField(max_length=120,blank=True,null=True) #max_length required
    
    
    other_exp_item_3 =  models.CharField(max_length=120,blank=True,null=True) #max_length required
    other_exp_amount_3 =  models.DecimalField(decimal_places=2,max_digits=1000,blank=True,null=True) 
    other_exp_billdetails_3 = models.CharField(max_length=120,blank=True,null=True) #max_length required
    #Total_amount_B  = models.DecimalField(decimal_places=2,max_digits=1000)
    
    no_of_enclosures = models.IntegerField()
    enclosure_date = models.CharField(max_length=10)
    #Eligible_Amount =  models.DecimalField(decimal_places=2,max_digits=1000)
    #AdvanceDraw =  models.DecimalField(decimal_places=2,max_digits=1000)
    #Net_Claim_Admissible =  models.DecimalField(decimal_places=2,max_digits=1000)
    #To_be_paid_by_iith =  models.DecimalField(decimal_places=2,max_digits=1000)
    #To_be_recovered_by_iith =  models.DecimalField(decimal_places=2,max_digits=1000)
    
    #payment_voucher_no = models.CharField(max_length=120) #max_length required
    #pymt_date = models.CharField(max_length=10)
    
    #amount =  models.DecimalField(decimal_places=2,max_digits=1000)
    #amt_in_words = models.CharField(max_length=120) #max_length required
    
    IFSC_Code   = models.CharField(max_length=12)
    Bank_name_branch = models.TextField()
    Bank_account_number = models.CharField(max_length=16)
    