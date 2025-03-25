from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Contract
from .forms import ContractForm
import os
from django.conf import settings


def checking_file(file):
    if file:
        file_name, file_extension = os.path.splitext(file.name)
        media_path = os.path.join(settings.MEDIA_ROOT, file.name)

        counter = 1
        while os.path.exists(media_path):
            new_name = f"{file_name}_{counter}{file_extension}"
            # media_path = os.path.join(settings.MEDIA_ROOT, new_name)
            counter += 1

            return new_name
    else:
        return


@permission_required('contracts.can_view_contract')
def contract_list(request):
    contracts = Contract.objects.all()
    return render(request, 'contracts-list.html', {'contracts': contracts})


@permission_required('contracts.can_add_contract')
def contract_create(request):
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES.get('document')
            uploaded_file.name = checking_file(uploaded_file)

            form.save()
            return redirect('contracts:contract_list')
    else:
        form = ContractForm()
    return render(request, 'contracts-create.html', {'form': form})


@permission_required('contracts.can_view_contract')
def contract_detail(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    return render(request, 'contracts-detail.html', {'object': contract})


@permission_required('contracts.can_change_contract')
def contract_update(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES, instance=contract)
        if form.is_valid():
            uploaded_file = request.FILES.get('document')
            if uploaded_file:
                uploaded_file.name = checking_file(uploaded_file)

            form.save()
            return redirect('contracts:contract_detail', pk=contract.pk)
    else:
        form = ContractForm(instance=contract)
    return render(request, 'contracts-edit.html', {'form': form, 'object': contract})


@permission_required('contracts.can_delete_contract')
def contract_delete(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        if contract.document:
            contract.document.delete(save=False)
        contract.delete()
        return redirect('contracts:contract_list')
    return render(request, 'contracts-delete.html', {'object': contract})
