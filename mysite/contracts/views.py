from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Contract
from .forms import ContractForm


@permission_required('contracts.view_contract')
def contract_list(request):
    contracts = Contract.objects.all()
    return render(request, 'contracts-list.html', {'contracts': contracts})


@permission_required('contracts.add_contract')
def contract_create(request):
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contracts:contract_list')
    else:
        form = ContractForm()
    return render(request, 'contracts-create.html', {'form': form})


@permission_required('contracts.view_contract')
def contract_detail(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    return render(request, 'contracts-detail.html', {'object': contract})


@permission_required('contracts.change_contract')
def contract_update(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contracts:contract_detail', pk=contract.pk)
    else:
        form = ContractForm(instance=contract)
    return render(request, 'contracts-edit.html', {'form': form, 'object': contract})


@permission_required('contracts.delete_contract')
def contract_delete(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        if contract.document:
            contract.document.delete(save=False)
        contract.delete()
        return redirect('contracts:contract_list')
    return render(request, 'contracts-delete.html', {'object': contract})
