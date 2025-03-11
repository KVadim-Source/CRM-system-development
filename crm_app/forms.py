from django import forms
from models import Service, AdCampaign, PotentialClient, Contract, ActiveClient
from django.contrib.auth.models import User, Group


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'description', 'cost')


class AdCampaignForm(forms.ModelForm):
    class Meta:
        model = AdCampaign
        fields = ('name', 'service', 'channel', 'budget')


class PotentialClientForm(forms.ModelForm):
    class Meta:
        model = PotentialClient
        fields = ('full_name', 'phone', 'email', 'ad_campaign')


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ('name', 'service', 'document_file', 'conclusion_date', 'period', 'amount')


class UserRoleForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    role = forms.ModelChoiceField(queryset=Group.objects.all())


class ActiveClientForm(forms.ModelForm):
    class Meta:
        model = ActiveClient
        fields = ('potential_client', 'contract')
