from django import forms
from .models import Actions

class ActionForm(forms.ModelForm):
    name        = forms.CharField(label='Name',widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    employee_id = forms.CharField(label='ID',widget=forms.TextInput(attrs={"placeholder":"Your employee_id"}))

    class Meta:
        model = Actions
        fields = [
            'name',
            'employee_id',
            ]
