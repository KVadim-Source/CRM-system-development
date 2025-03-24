from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Product
from ads.models import Advertisement
from leads.models import Lead
from customers.models import Customer


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

    return render(request, 'index.html', context)
