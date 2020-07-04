from django.db import models
CHOICES = (
    ('Air(Business)','Air(Business)'),
    ('Air(Economy)','Air(Economy)'),
    ('Train(1AC)', 'Train(1AC)'),
    ('Train(2AC)', 'Train(2AC)'),
    ('Train(3AC)', 'Train(3AC)'),
    ('Train(ACC)', 'Train(ACC)'),
    ('Train(SL)', 'Train(SL)'),
    ('Train(CC)', 'Train(CC)'),
    ('Road (AC)','Road (AC)'),
    ('Road (Non-AC)','Road (Non-AC)'),
)
# Create your models here.
class Travel_adv(models.Model):
    name        = models.CharField(max_length=120) #max_length required
    designation = models.CharField(max_length=120) #max_length required
    department  = models.CharField(max_length=120) #max_length required
    employee_id = models.CharField(max_length=20) #max_length required
    basic_pay   = models.DecimalField(decimal_places=2,max_digits=1000) 

    journeyclass = models.CharField(max_length=60, choices=CHOICES, default='Road (AC)')
    dt1      = models.CharField(max_length=10)
    dt2      = models.CharField(max_length=10)
    purpose  = models.TextField() 
    other_expenditures = models.DecimalField(decimal_places=2,max_digits=1000)
    details = models.CharField(max_length=120) #max_length required
    Total_amount      = models.DecimalField(decimal_places=2,max_digits=1000)

    IFSC_Code   = models.CharField(max_length=12)
    Bank_name_branch = models.TextField()
    Bank_account_number = models.CharField(max_length=16)
