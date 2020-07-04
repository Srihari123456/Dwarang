from django import forms

from .models import Contingent_exp

class ContingentForm(forms.ModelForm):
    dt1       = forms.CharField(label='Date',widget=forms.TextInput(attrs={"placeholder":"Date"}))
    description1 = forms.CharField(label='Purpose',required=False,widget=forms.Textarea(attrs={"placeholder":"Your description","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))

    amount1       = forms.DecimalField(initial=0.00)  


    dt2       = forms.CharField(label='Date',required=False,widget=forms.TextInput(attrs={"placeholder":"Date"}))
    description2 = forms.CharField(required=False,widget=forms.Textarea(attrs={"placeholder":"Your description","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    amount2       = forms.DecimalField(initial=0.00)    
    
    dt3       = forms.CharField(label='Date',required=False,widget=forms.TextInput(attrs={"placeholder":"Date"}))
    description3 = forms.CharField(required=False,widget=forms.Textarea(attrs={"placeholder":"Your description","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    amount3       = forms.DecimalField(initial=0.00)    
    
    Total_amount       = forms.DecimalField(initial=0.00)
    #totamount = amount1+amount2+amount3
    
    amount_words = forms.CharField(required=False,widget=forms.Textarea(attrs={"placeholder":"Amount in words","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    station     = forms.CharField(label='Station',widget=forms.TextInput(attrs={"placeholder":"Your Station"}))
    name        = forms.CharField(label='Name',widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    employee_id = forms.CharField(label='ID', widget=forms.TextInput(attrs={"placeholder": "Your ID"}))
    address =  forms.CharField(required=False,widget=forms.Textarea(attrs={"placeholder":"Address","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    
    IFSC_Code   = forms.CharField(label='IFSC Code',widget=forms.TextInput(attrs={"placeholder":"IFSC Code"}))
    Bank_name_branch = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your description", "class": "new-class-name two",
                                     "id": "my-id-for-textarea", "rows": 5, 'cols': 19}))
    Bank_account_number = forms.CharField(label='Bank Account Number',widget=forms.TextInput(attrs={"placeholder": "Bank Account Number"}))
                        
    
    
    class Meta:
        model = Contingent_exp
        fields = [
            'name',
            'employee_id',
            'address',
            'dt1',
            'description1',
            'amount1',
            'dt2',
            'description2',
            'amount2',
            'dt3',
            'description3',
            'amount3',
            'Total_amount',
            'amount_words',
            'station',
            'IFSC_Code',
            'Bank_name_branch',
            'Bank_account_number',
        ]
