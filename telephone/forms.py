from django import forms

from .models import Telephone_Reim

class TelephoneForm(forms.ModelForm):
    name        = forms.CharField(label='Name',widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    employee_id = forms.CharField(label='ID', widget=forms.TextInput(attrs={"placeholder": "Your employee_id"}))
    designation = forms.CharField(label='Designation',widget=forms.TextInput(attrs={"placeholder":"Your Designation"}))
    department  = forms.CharField(label='Department',widget=forms.TextInput(attrs={"placeholder":"Your department"}))
    IFSC_Code   = forms.CharField(label='IFSC Code',widget=forms.TextInput(attrs={"placeholder":"IFSC Code"}))
    month       = forms.CharField(label='Month to Reimburse',widget=forms.TextInput(attrs={"placeholder":"Month to Reimburse"}))
    cred_month  = forms.CharField(label='Month to credit',widget=forms.TextInput(attrs={"placeholder":"Month to credit"}))
    
    
    Bank_name_branch = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Bank's Name and Branch","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
    Bank_account_number = forms.CharField(label='Bank Account Number',widget=forms.TextInput(attrs={"placeholder":"Bank Account Number"}))
                 
    amount_words = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Enter the amount in words","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))
                        
    
    amount       = forms.DecimalField(initial=0.00)
    class Meta:
        model = Telephone_Reim
        fields = [
            'name',
            'employee_id',
            'designation',
            'department',
            'employee_id',
            'IFSC_Code',
            'month',
            'cred_month',
            'Bank_name_branch',
            'Bank_account_number',
            'amount_words',
            'amount',
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
