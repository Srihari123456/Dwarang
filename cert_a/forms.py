from django import forms

from .models import Cert_A

class CertForm(forms.ModelForm):
    name        = forms.CharField(label='Name*',widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    designation = forms.CharField(label='Designation*',widget=forms.TextInput(attrs={"placeholder":"Your Designation"}))
    employee_id = forms.CharField(label='ID*',widget=forms.TextInput(attrs={"placeholder":"Your employee_id"}))
    patient_name= forms.CharField(label='Patient Name*',widget=forms.TextInput(attrs={"placeholder":"Patient Name"}))
    patient_age = forms.IntegerField(label='Patient Age*')
    employee_rel= forms.CharField(label='Relation with employee*',widget=forms.TextInput(attrs={"placeholder":"Relation with employee"}))
    disease     = forms.CharField(label='Disease*',widget=forms.TextInput(attrs={"placeholder":"Disease"}))
    dt1        = forms.CharField(label='From Date*',widget=forms.TextInput(attrs={"placeholder":"From Date"}))
    dt2        = forms.CharField(label='To Date*',widget=forms.TextInput(attrs={"placeholder":"To Date"}))
    doctor_address = forms.CharField(label='Doctor Address*',widget=forms.Textarea(attrs={"placeholder":"Doctor's Address with Name","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    
    Consult_dt1  = forms.CharField(label='Consultation Date*',widget=forms.TextInput(attrs={"placeholder":"Consultation Date-1"}))
    Consult_fee1 = forms.DecimalField(label='Consultation Fee*',initial=0.00,required=False)
    Injection_fee1     = forms.DecimalField(label='Injection Fee*',initial=0.00,required=False)
    
    Consult_dt2  = forms.CharField(label='Consultation Date',required=False,widget=forms.TextInput(attrs={"placeholder":"Consultation Date-2"}))
    Consult_fee2 = forms.DecimalField(label='Consultation Fee',initial=0.00,required=False)
    Injection_fee2     = forms.DecimalField(label='Injection Fee',initial=0.00,required=False)
    
    Med_name1      = forms.CharField(label='Medicine*',widget=forms.TextInput(attrs={"placeholder":"Medicine"}))
    Quantity1       = forms.IntegerField(label='Quantity*')
    Price1     = forms.DecimalField(label='Price*',initial=0.00)
    Med_CashMemoNo1 = forms.CharField(label='Cash Memo Number*',widget=forms.TextInput(attrs={"placeholder":" Cash Memo Number"}))
    
    Med_name2      = forms.CharField(required=False,label='Medicine',widget=forms.TextInput(attrs={"placeholder":"Medicine"}))
    Quantity2       = forms.IntegerField(label='Quantity',required=False)
    Price2     = forms.DecimalField(initial=0.00,required=False,label='Price')
    Med_CashMemoNo2 = forms.CharField(required=False,label='Cash Memo Number',widget=forms.TextInput(attrs={"placeholder":"Cash Memo Number"}))
    
    
    DiagTest_name1   = forms.CharField(label='Diagnostic Test* ',widget=forms.TextInput(attrs={"placeholder":"Diagnostic Test Name"}))
    DiagTest_center1 = forms.CharField(label='Diagnostic Center* ',widget=forms.TextInput(attrs={"placeholder":"Diagnostic Center Name"}))
    Diagnostic_Test_price1  = forms.DecimalField(label='Price*',initial=0.00)
    
    
    DiagTest_name2   = forms.CharField(required=False,label='Diagnostic Test ',widget=forms.TextInput(attrs={"placeholder":"Diagnostic Test Name"}))
    DiagTest_center2 = forms.CharField(required=False,label='Diagnostic Center ',widget=forms.TextInput(attrs={"placeholder":"Diagnostic Center Name"}))
    Diagnostic_Test_price2  = forms.DecimalField(label='Price',initial=0.00,required=False)
   
    RefDoc =  forms.CharField(max_length=120,label='Doctor Referred*') #max_length required
    station = forms.CharField(max_length=120,label='Station*') #max_length required
    
    Total_amount       = forms.DecimalField(label='Total Amount*',initial=0.00)
    class Meta:
        model = Cert_A
        fields = [
            'name',
            'designation',
            'employee_id',
            'patient_name',
            'patient_age',
            'employee_rel',
            'disease',
            'dt1',
            'dt2',
            'doctor_address',
            'Consult_dt1','Consult_fee1','Injection_fee1',
            'Consult_dt2','Consult_fee2','Injection_fee2',
            'Med_name1','Quantity1', 'Price1','Med_CashMemoNo1',
            'Med_name2','Quantity2','Price2','Med_CashMemoNo2',
            'DiagTest_name1','DiagTest_center1','Diagnostic_Test_price1',
            'DiagTest_name2','DiagTest_center2','Diagnostic_Test_price2',
            'RefDoc',
            'station',
            'Total_amount',
        ]
