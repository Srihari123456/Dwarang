from django import forms

from .models import Travel_adv
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

class TravelForm(forms.ModelForm):
    name        = forms.CharField(label='Name*',widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    designation = forms.CharField(label='Designation*',widget=forms.TextInput(attrs={"placeholder":"Your Designation"}))
    department  = forms.CharField(label='Department*',widget=forms.TextInput(attrs={"placeholder":"Your department"}))
    dt1        = forms.CharField(label='From Date*',widget=forms.TextInput(attrs={"placeholder":"From Date"}))
    dt2        = forms.CharField(label='To Date*',widget=forms.TextInput(attrs={"placeholder":"To Date"}))
    basic_pay       = forms.DecimalField(label='Basic Pay*',initial=0.00)
    #accomodation_charges       = forms.DecimalField(initial=0.00)
    other_expenditures = forms.DecimalField(label='Other Expenditures*',initial=0.00)
    details  = forms.CharField(label='Details*',widget=forms.TextInput(attrs={"placeholder":"Details"}))
    employee_id = forms.CharField(label='ID*',widget=forms.TextInput(attrs={"placeholder":"Your employee_id"}))
    IFSC_Code   = forms.CharField(label='IFSC Code*',widget=forms.TextInput(attrs={"placeholder":"IFSC Code"}))
    journeyclass = forms.ChoiceField(label='Class of Journey*',choices=CHOICES,required=True)
    purpose = forms.CharField(label='Purpose*',widget=forms.Textarea(attrs={"placeholder":"Purpose","class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea","rows"       : 5,'cols'       : 19}))

    Bank_name_branch = forms.CharField(label='Bank Name and Branch*',widget=forms.Textarea(attrs={"placeholder": "Your description", "class": "new-class-name two",
                                     "id": "my-id-for-textarea", "rows": 5, 'cols': 19}))
    Bank_account_number =  forms.CharField(label='Bank Account Number*',widget=forms.TextInput(attrs={"placeholder":"Bank Account Number"}))

    
    Total_amount       = forms.DecimalField(label='Total Amount*',initial=0.00)
    class Meta:
        model = Travel_adv
        fields = [
            'name',
            'employee_id',
            'designation',

            'department',
            'basic_pay',
            'dt1',
            'dt2',
            'purpose',
            'journeyclass',
            'other_expenditures',
            'details',

            'Total_amount',

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
class RawTravelForm(forms.Form):
    name        = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    designation = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Your Designation"}))
    department  = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Your department"}))
    dt1        = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"From Date"}))
    dt2        = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"To Date"}))
    basic_pay       = forms.DecimalField(initial=0.00)
    accomodation_charges       = forms.DecimalField(initial=0.00)
    other_expenditures = forms.DecimalField(initial=0.00)
    details  = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    employee_id = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Your employee_id"}))
    IFSC_Code   = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"IFSC Code"}))
    #journeyclass = forms.ModelMultipleChoiceField(widget = forms.RadioSelect,queryset = Travel_adv_choices.objects.all())
    journeyclass = forms.ChoiceField(choices=CHOICES,required=True)
#    widget=forms.SelectMultiple())
    
    #CharField(label='', choices=COLOR_CHOICES, default='green')          forms.CheckboxSelectMultiple
    purpose = forms.CharField(
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder":"Your description",
                                    "class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea",
                                    "rows"       : 5,
                                    'cols'       : 30
                                    }
                            )
                        )
    
    Bank_name_branch = forms.CharField(
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder":"Your description",
                                    "class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea",
                                    "rows"       : 5,
                                    'cols'       : 30
                                    }
                            )
                        )
    Bank_account_number = forms.CharField(
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder":"Your description",
                                    "class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea",
                                    "rows"       : 5,
                                    'cols'       : 30
                                    }
                            )
                        )
                 
    amount_words = forms.CharField(
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder":"Your description",
                                    "class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea",
                                    "rows"       : 5,
                                    'cols'       : 30
                                    }
                            )
                        )
                        
    
    totamount       = forms.DecimalField(initial=0.00)
"""
    title       = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder":"Your description",
                                    "class"      : "new-class-name two",
                                    "id"         : "my-id-for-textarea",
                                    "rows"       : 10,
                                    'cols'       : 30
                                    }
                            )
                        )
    price       = forms.DecimalField(initial=100.50)
"""    