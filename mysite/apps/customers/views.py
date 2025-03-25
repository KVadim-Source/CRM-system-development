from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Customer
from .forms import CustomerForm


@permission_required('customers.can_view_customer')
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers-list.html', {'customers': customers})


@permission_required('customers.can_add_customer')
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('customers:customer_detail', pk=customer.pk)
    else:
        form = CustomerForm()
    return render(request, 'customers-create.html', {'form': form})


@permission_required('customers.can_view_customer')
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customers-detail.html', {'object': customer})


@permission_required('customers.can_change_customer')
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers:customer_detail', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers-edit.html', {'form': form, 'object': customer})


@permission_required('customers.can_delete_customer')
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers:customer_list')
    return render(request, 'customers-delete.html', {'object': customer})
