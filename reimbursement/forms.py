from django import forms

from .models import Reimbursement

class ReimbursementForm(forms.ModelForm):
    name        = forms.CharField(label='Name',widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    employee_id = forms.CharField(label='ID', widget=forms.TextInput(attrs={"placeholder": "Your ID"}))
    department  = forms.CharField(label='Department',widget=forms.TextInput(attrs={"placeholder":"Your department"}))
    net_claimed = forms.DecimalField(initial=0.00)  
    
    dt1       = forms.CharField(label='Date',widget=forms.TextInput(attrs={"placeholder":"Date"}))
    cashmemo1 = forms.CharField(label='Cash memo',required=True,widget=forms.Textarea(attrs={"placeholder":"Cash memo","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    firmname1 = forms.CharField(label='Firm Name',required=True,widget=forms.Textarea(attrs={"placeholder":"Firm Name","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    purpose1 =  forms.CharField(label='Purpose',required=True,widget=forms.Textarea(attrs={"placeholder":"Purpose","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    amount1  = forms.DecimalField(initial=0.00)  


    dt2       = forms.CharField(label='Date',required=False,widget=forms.TextInput(attrs={"placeholder":"Date"}))
    cashmemo2 = forms.CharField(label='Cash memo',required=False,widget=forms.Textarea(attrs={"placeholder":"Cash memo","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    firmname2 = forms.CharField(label='Firm Name',required=False,widget=forms.Textarea(attrs={"placeholder":"Firm Name","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    purpose2 =  forms.CharField(label='Purpose',required=False,widget=forms.Textarea(attrs={"placeholder":"Purpose","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    amount2  = forms.DecimalField(initial=0.00)  

    
    dt3       = forms.CharField(label='Date',required=False,widget=forms.TextInput(attrs={"placeholder":"Date"}))
    cashmemo3 = forms.CharField(label='Cash memo',required=False,widget=forms.Textarea(attrs={"placeholder":"Cash memo","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    firmname3 = forms.CharField(label='Firm Name',required=False,widget=forms.Textarea(attrs={"placeholder":"Firm Name","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    purpose3 =  forms.CharField(label='Purpose',required=False,widget=forms.Textarea(attrs={"placeholder":"Purpose","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    amount3  = forms.DecimalField(initial=0.00)  

    dt4       = forms.CharField(label='Date',required=False,widget=forms.TextInput(attrs={"placeholder":"Date"}))
    cashmemo4 = forms.CharField(label='Cash memo',required=False,widget=forms.Textarea(attrs={"placeholder":"Cash memo","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    firmname4 = forms.CharField(label='Firm Name',required=False,widget=forms.Textarea(attrs={"placeholder":"Firm Name","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    purpose4 =  forms.CharField(label='Purpose',required=False,widget=forms.Textarea(attrs={"placeholder":"Purpose","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    amount4  = forms.DecimalField(initial=0.00)  

    
    dt5       = forms.CharField(label='Date',required=False,widget=forms.TextInput(attrs={"placeholder":"Date"}))
    cashmemo5 = forms.CharField(label='Cash memo',required=False,widget=forms.Textarea(attrs={"placeholder":"Cash memo","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    firmname5 = forms.CharField(label='Firm Name',required=False,widget=forms.Textarea(attrs={"placeholder":"Firm Name","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    purpose5 =  forms.CharField(label='Purpose',required=False,widget=forms.Textarea(attrs={"placeholder":"Purpose","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    amount5  = forms.DecimalField(initial=0.00)  
    
     
    
    Total_amount       = forms.DecimalField(initial=0.00)
    #totamount = amount1+amount2+amount3
    
    amount_words = forms.CharField(label='Amount in words',widget=forms.Textarea(attrs={"placeholder":"Your description","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
        
     
    IFSC_Code   = forms.CharField(label='IFSC Code',widget=forms.TextInput(attrs={"placeholder":"IFSC Code"}))
    Bank_name_branch =  forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Your description","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    Bank_account_number =  forms.CharField(label='Bank Account Number',widget=forms.TextInput(attrs={"placeholder":"Bank Account Number"}))
                        
    
    
    class Meta:
        model = Reimbursement
        fields = [
            'name',
            'employee_id',
            'department',
            'dt1',
            'cashmemo1',
            'firmname1',
            'purpose1',
            'amount1',
            
            'dt2',
            'cashmemo2',
            'firmname2',
            'purpose2',
            'amount2',
            
            'dt3',
            'cashmemo3',
            'firmname3',
            'purpose3',
            'amount3',
            
            'dt4',
            'cashmemo4',
            'firmname4',
            'purpose4',
            'amount4',
            
            'dt5',
            'cashmemo5',
            'firmname5',
            'purpose5',
            'amount5',
            'net_claimed',

            'Total_amount',
            'amount_words',
            'IFSC_Code',
            'Bank_name_branch',
            'Bank_account_number',
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
