from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from apps.products.models import Product
from apps.ads.models import Advertisement
from apps.leads.models import Lead
from apps.customers.models import Customer


def custom_logout(request):
    logout(request)
    return redirect('/accounts/login/')


@login_required
def index(request):
    products_count = Product.objects.count()
    advertisements_count = Advertisement.objects.count()
    leads_count = Lead.objects.count()
    customers_count = Customer.objects.count()

    context = {
        'products_count': products_count,
        'advertisements_count': advertisements_count,
        'leads_count': leads_count,
        'customers_count': customers_count,
    }

    return render(request, 'users/index.html', context)
