from django import forms

from .models import TA_Bill
CHOICES = (
    ('-','-'),
    ('Air','Air'),
    ('Rail', 'Rail'),
    ('Road','Road'),

    
)
class TAForm(forms.ModelForm):
    name        = forms.CharField(label='Name*',widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    employee_id = forms.CharField(label='ID*',widget=forms.TextInput(attrs={"placeholder":"Your employee_id"}))
    designation = forms.CharField(label='Designation*',widget=forms.TextInput(attrs={"placeholder":"Your Designation"}))
    department = forms.CharField(label='Department*',widget=forms.TextInput(attrs={"placeholder":"Your Department"}))
    institute = forms.CharField(label='Institute*',widget=forms.TextInput(attrs={"placeholder":"Your Institute"})) #max_length required
    basicpay = forms.DecimalField(decimal_places=2,label='Basic Pay*',max_digits=1000)
    institute_acc_no = forms.CharField(label='Institute Account Number*',widget=forms.TextInput(attrs={"placeholder":"Institute Account Number"})) #max_length required
    purpose = forms.CharField(label='Purpose*',required=True,widget=forms.Textarea(attrs={"placeholder":"Purpose of Journey","class"      : "new-class-name two",
                "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    dep_station_1 = forms.CharField(label='Departure Station*',widget=forms.TextInput(attrs={"placeholder":"Departure Station"})) #max_length required
    dep_date_1 = forms.CharField(label='Departure Date*',widget=forms.TextInput(attrs={"placeholder":"Departure Date"}))
    arr_station_1 = forms.CharField(label='Arrival Station*',widget=forms.TextInput(attrs={"placeholder":"Arrival Station"})) #max_length required
    arr_date_1 = forms.CharField(label='Arrival Date*',widget=forms.TextInput(attrs={"placeholder":"Arrival Date"}))
    
    mode_of_journey_1 = forms.ChoiceField(label='Mode of Journey*',choices=CHOICES)
    ticket_no_1 = forms.CharField(label='Ticket Number*',widget=forms.TextInput(attrs={"placeholder":"Ticket Number"})) #max_length required
    fare_1 =  forms.DecimalField(label='Fare*',initial=0.00)
    
    dep_station_2 = forms.CharField(required=False,label='Departure Station',widget=forms.TextInput(attrs={"placeholder":"Departure Station"})) #max_length required
    dep_date_2 = forms.CharField(required=False,label='Departure Date',widget=forms.TextInput(attrs={"placeholder":"Departure Date "}))
    
    arr_station_2 = forms.CharField(required=False,label='Arrival Station',widget=forms.TextInput(attrs={"placeholder":"Arrival Station "})) #max_length required
    arr_date_2 = forms.CharField(required=False,label='Arrival Date',widget=forms.TextInput(attrs={"placeholder":"Arrival Date "}))
    
    mode_of_journey_2 = forms.ChoiceField(label='Mode of Journey',required=False,choices=CHOICES)
    ticket_no_2 = forms.CharField(required=False,label='Ticket Number',widget=forms.TextInput(attrs={"placeholder":"Ticket Number "})) #max_length required
    fare_2 =  forms.DecimalField(label='Fare',required=False,initial=0.00)

    dep_station_3 = forms.CharField(required=False,label='Departure Station',widget=forms.TextInput(attrs={"placeholder":"Departure Station "})) #max_length required
    dep_date_3 = forms.CharField(required=False,label='Departure Date',widget=forms.TextInput(attrs={"placeholder":"Departure Date "}))
    
    arr_station_3 = forms.CharField(required=False,label='Arrival Station',widget=forms.TextInput(attrs={"placeholder":"Arrival Station "})) #max_length required
    arr_date_3 = forms.CharField(required=False,label='Arrival Date',widget=forms.TextInput(attrs={"placeholder":"Arrival Date "}))
    
    mode_of_journey_3 = forms.ChoiceField(label='Mode of Journey',required=False, choices=CHOICES)
    ticket_no_3 = forms.CharField(required=False,label='Ticket Number',widget=forms.TextInput(attrs={"placeholder":"Ticket Number - 3"})) #max_length required
    fare_3 =  forms.DecimalField(label='Fare',required=False,initial=0.00)

    Total_amount_A  = forms.DecimalField(label='Total Amount(A)*',initial=0.00)
    
    other_exp_item_1 = forms.CharField(label='Expenditure Item*',widget=forms.TextInput(attrs={"placeholder":"Item of Expenditure"})) #max_length required
    other_exp_amount_1 =  forms.DecimalField(label='Amount*',initial=0.00)
    other_exp_billdetails_1 = forms.CharField(label='Cash Bill Details*',widget=forms.TextInput(attrs={"placeholder":"Cash Bill Details"})) #max_length required
    
    
    other_exp_item_2 = forms.CharField(required=False,label='Expenditure Item',widget=forms.TextInput(attrs={"placeholder":"Item of Expenditure"})) #max_length required
    other_exp_amount_2 =  forms.DecimalField(label='Amount',required=False,initial=0.00)
    other_exp_billdetails_2 = forms.CharField(required=False,label='Cash Bill Details',widget=forms.TextInput(attrs={"placeholder":"Cash Bill Details"})) #max_length required
    
    
    other_exp_item_3 =  forms.CharField(required=False,label='Expenditure Item',widget=forms.TextInput(attrs={"placeholder":"Item of Expenditure"})) #max_length required
    other_exp_amount_3 =  forms.DecimalField(label='Amount',required=False,initial=0.00)
    other_exp_billdetails_3 = forms.CharField(required=False,label='Cash Bill Details',widget=forms.TextInput(attrs={"placeholder":"Cash Bill Details"})) #max_length required
    Total_amount_B = forms.DecimalField(label='Total Amount(B)*',initial=0.00)
    
    no_of_enclosures = forms.IntegerField(label='No.of Enclosures*',)
    enclosure_date = forms.CharField(label='Enclosure Date*',
                                 widget=forms.TextInput(attrs={"placeholder": "Enclosure Date"}))
    Eligible_Amount =  forms.DecimalField(label='Eligible Amount*',initial=0.00)
    AdvanceDraw =  forms.DecimalField(label='Advance Draw*',initial=0.00)
    Net_Claim_Admissible =  forms.DecimalField(label='Net Claim Admissible*',initial=0.00)
    To_be_paid_by_iith =  forms.DecimalField(label='To be paid by iith*',initial=0.00)
    To_be_recovered_by_iith =  forms.DecimalField(label='To be recovered by iith*',initial=0.00)
    
    amount =  forms.DecimalField(initial=0.00,label='Amount*')
    amt_in_words = forms.CharField(label='Amount in words*',widget=forms.TextInput(attrs={"placeholder":"Amount in words"})) #max_length required
    
    IFSC_Code   = forms.CharField(label='IFSC Code*',widget=forms.TextInput(attrs={"placeholder":"IFSC Code"})) #max_length required
    Bank_name_branch = forms.CharField(label='Bank Name and Branch*',widget=forms.Textarea(attrs={"placeholder":"Bank name branch","class"      : "new-class-name two",
                "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    Bank_account_number = forms.CharField(label='Bank Account Number*',widget=forms.TextInput(attrs={"placeholder":"Bank Account Number"}))
    
   
    class Meta:
        model = TA_Bill
        fields = [
            'name','employee_id','designation',
            'department','institute','basicpay',
            'institute_acc_no','purpose',
            'dep_station_1','dep_date_1','arr_station_1','arr_date_1',
            'mode_of_journey_1', 'ticket_no_1', 'fare_1',
            'dep_station_2','dep_date_2','arr_station_2','arr_date_2',
            'mode_of_journey_2', 'ticket_no_2', 'fare_2',
            'dep_station_3','dep_date_3','arr_station_3','arr_date_3',
            'mode_of_journey_3', 'ticket_no_3', 'fare_3',


            'Total_amount_A',
            'other_exp_item_1',            'other_exp_amount_1',            'other_exp_billdetails_1',
            'other_exp_item_2',            'other_exp_amount_2',            'other_exp_billdetails_2',
            'other_exp_item_3',            'other_exp_amount_3',            'other_exp_billdetails_3',            
            'Total_amount_B',
            'no_of_enclosures',  'enclosure_date',    'Eligible_Amount',    'AdvanceDraw',
            'Net_Claim_Admissible', 'To_be_paid_by_iith', 'To_be_recovered_by_iith',
            'amount',   'amt_in_words',
            'IFSC_Code',            'Bank_name_branch',            'Bank_account_number',
        ]
"""        
    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get("title")
        if not "CEG" in title:
            raise forms.ValidationError("This is not a valid title")
        return title
        
    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        if not "CEG" in email:
            raise forms.ValidationError("This is not a valid email")
        if not email.endswith("com"):
            raise forms.ValidationError("This is not a valid email")
        return title
"""