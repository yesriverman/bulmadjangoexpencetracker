from django import forms
from .models import *

class ExpenseForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    class Meta:
        model = Expense
        fields = ['label', 'amount', 'date']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Group name'}),}

class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name', 'group', 'monthly_expected_amount']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Label name'}),
            'group': forms.Select(attrs={'class': 'input'}),
            'monthly_expected_amount': forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Optional expected monthly amount'}),}

class IncomeForm(forms.ModelForm):
    # date = forms.DateField(
    #             widget=forms.DateInput(attrs={'type': 'date'}),
    #             required=True
    #         )
    
    class Meta:
        model = Income
        fields = ["amount", "date"]
        widgets = {"date": forms.DateInput(attrs={"type": "date"})}

        


