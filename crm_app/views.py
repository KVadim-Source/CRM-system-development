from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, Permission
from models import Service, AdCampaign, PotentialClient, Contract, ActiveClient
from forms import ServiceForm, AdCampaignForm, PotentialClientForm, ContractForm, ActiveClientForm


def create_roles():
    admin_group, created = Group.objects.get_or_create(name='admin')
    operator_group, created = Group.objects.get_or_create(name='operator')
    marketer_group, created = Group.objects.get_or_create(name='marketer')
    manager_group, created = Group.objects.get_or_create(name='manager')

    admin_permissions = [
        Permission.objects.get(codename='view_user'),
        Permission.objects.get(codename='add_user'),
        Permission.objects.get(codename='change_user'),
        Permission.objects.get(codename='delete_user'),
    ]
    operator_permissions = [
        Permission.objects.get(codename='view_potentialclient'),
        Permission.objects.get(codename='add_potentialclient'),
        Permission.objects.get(codename='change_potentialclient'),
    ]
    marketer_permissions = [
        Permission.objects.get(codename='view_service'),
        Permission.objects.get(codename='add_service'),
        Permission.objects.get(codename='change_service'),
        Permission.objects.get(codename='view_adcampaign'),
        Permission.objects.get(codename='add_adcampaign'),
        Permission.objects.get(codename='change_adcampaign'),
    ]
    manager_permissions = [
        Permission.objects.get(codename='view_contract'),
        Permission.objects.get(codename='add_contract'),
        Permission.objects.get(codename='change_contract'),
        Permission.objects.get(codename='view_potentialclient'),
    ]

    admin_group.permissions.set(admin_permissions)
    operator_group.permissions.set(operator_permissions)
    marketer_group.permissions.set(marketer_permissions)
    manager_group.permissions.set(manager_permissions)


def assign_role(user, role_name):
    role_group = Group.objects.get(name=role_name)
    user.groups.add(role_group)


def check_role(user, role_name):
    role_group = Group.objects.get(name=role_name)
    return role_group in user.groups.all()


@login_required
@permission_required('crm_app.view_service')
def services_list(request):
    if check_role(request.user, 'marketer'):
        services = Service.objects.all()
        return render(request, 'services_list.html', {'services': services})
    else:
        return redirect('home')


@login_required
def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services_list')
    else:
        form = ServiceForm()
    return render(request, 'create_service.html', {'form': form})


@login_required
def service_detail(request, pk):
    service = Service.objects.get(pk=pk)
    return render(request, 'service_detail.html', {'service': service})


@login_required
def edit_service(request, pk):
    service = Service.objects.get(pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('services_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'edit_service.html', {'form': form})


@login_required
def ad_campaigns_list(request):
    campaigns = AdCampaign.objects.all()
    return render(request, 'ad_campaigns_list.html', {'campaigns': campaigns})


@login_required
def ad_campaign_detail(request, pk):
    campaign = AdCampaign.objects.get(pk=pk)
    return render(request, 'ad_campaign_detail.html', {'campaign': campaign})


@login_required
def edit_ad_campaign(request, pk):
    campaign = AdCampaign.objects.get(pk=pk)
    if request.method == 'POST':
        form = AdCampaignForm(request.POST, instance=campaign)
        if form.is_valid():
            form.save()
            return redirect('ad_campaigns_list')
    else:
        form = AdCampaignForm(instance=campaign)
    return render(request, 'edit_ad_campaign.html', {'form': form})


@login_required
def delete_ad_campaign(request, pk):
    campaign = AdCampaign.objects.get(pk=pk)
    campaign.delete()
    return redirect('ad_campaigns_list')


@login_required
def create_ad_campaign(request):
    if request.method == 'POST':
        form = AdCampaignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ad_campaigns_list')
    else:
        form = AdCampaignForm()
    return render(request, 'create_ad_campaign.html', {'form': form})


@login_required
def potential_clients_list(request):
    clients = PotentialClient.objects.all()
    return render(request, 'potential_clients_list.html', {'clients': clients})


@login_required
def create_potential_client(request):
    if request.method == 'POST':
        form = PotentialClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('potential_clients_list')
    else:
        form = PotentialClientForm()
    return render(request, 'create_potential_client.html', {'form': form})


@login_required
def contracts_list(request):
    contracts = Contract.objects.all()
    return render(request, 'contracts_list.html', {'contracts': contracts})


@login_required
def contract_detail(request, pk):
    contract = Contract.objects.get(pk=pk)
    return render(request, 'contract_detail.html', {'contract': contract})


@login_required
def edit_contract(request, pk):
    contract = Contract.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contracts_list')
    else:
        form = ContractForm(instance=contract)
    return render(request, 'edit_contract.html', {'form': form})


@login_required
def delete_contract(request, pk):
    contract = Contract.objects.get(pk=pk)
    contract.delete()
    return redirect('contracts_list')


@login_required
def create_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contracts_list')
    else:
        form = ContractForm()
    return render(request, 'create_contract.html', {'form': form})


@login_required
def delete_service(request, pk):
    service = Service.objects.get(pk=pk)
    service.delete()
    return redirect('services_list')


@login_required
def convert_to_active_client(request, pk):
    potential_client = PotentialClient.objects.get(pk=pk)
    contract = Contract.objects.create(name="Contract for " + potential_client.full_name)
    ActiveClient.objects.create(potential_client=potential_client, contract=contract)
    return redirect('active_clients_list')


@login_required
def active_clients_list(request):
    clients = ActiveClient.objects.all()
    return render(request, 'active_clients_list.html', {'clients': clients})


@login_required
def active_client_detail(request, pk):
    client = ActiveClient.objects.get(pk=pk)
    return render(request, 'active_client_detail.html', {'client': client})


@login_required
def edit_active_client(request, pk):
    client = ActiveClient.objects.get(pk=pk)
    if request.method == 'POST':
        form = ActiveClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('active_clients_list')
    else:
        form = ActiveClientForm(instance=client)
    return render(request, 'edit_active_client.html', {'form': form})


@login_required
def delete_active_client(request, pk):
    client = ActiveClient.objects.get(pk=pk)
    client.delete()
    return redirect('active_clients_list')


@login_required
def create_active_client(request, pk):
    potential_client = PotentialClient.objects.get(pk=pk)
    if request.method == 'POST':
        form = ActiveClientForm(request.POST)
        if form.is_valid():
            active_client = form.save(commit=False)
            active_client.potential_client = potential_client
            active_client.save()
            return redirect('active_clients_list')
    else:
        form = ActiveClientForm(initial={'potential_client': potential_client})
    return render(request, 'create_active_client.html', {'form': form})


@login_required
def ad_campaign_stats(request):
    campaigns = AdCampaign.objects.all()
    stats = []
    for campaign in campaigns:
        potential_clients_count = PotentialClient.objects.filter(ad_campaign=campaign).count()
        active_clients_count = ActiveClient.objects.filter(potential_client__ad_campaign=campaign).count()
        contracts = Contract.objects.filter(service__ad_campaign=campaign)
        total_revenue = sum(contract.amount for contract in contracts)
        stats.append({
            'campaign': campaign,
            'potential_clients': potential_clients_count,
            'active_clients': active_clients_count,
            'total_revenue': total_revenue,
            'budget': campaign.budget
        })
    return render(request, 'ad_campaign_stats.html', {'stats': stats})
