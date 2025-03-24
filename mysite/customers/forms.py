from django import forms
from .models import Customer
from leads.models import Lead


class CustomerForm(forms.ModelForm):
    lead = forms.ModelChoiceField(queryset=Lead.objects.all(), label='Лид')

    class Meta:
        model = Customer
        fields = ['lead', 'advertisement']
