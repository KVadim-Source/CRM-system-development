from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Advertisement
from .forms import AdvertisementForm


@permission_required('ads.can_view_advertisement')
def advertisement_list(request):
    ads = Advertisement.objects.all()
    return render(request, 'ads-list.html', {'ads': ads})


@permission_required('ads.can_add_advertisement')
def advertisement_create(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ads:advertisement_list')
    else:
        form = AdvertisementForm()
    return render(request, 'ads-create.html', {'form': form})


@permission_required('ads.can_view_advertisement')
def advertisement_detail(request, pk):
    ad = get_object_or_404(Advertisement, pk=pk)
    return render(request, 'ads-detail.html', {'object': ad})


@permission_required('ads.can_change_advertisement')
def advertisement_update(request, pk):
    ad = get_object_or_404(Advertisement, pk=pk)
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ads:advertisement_detail', pk=ad.pk)
    else:
        form = AdvertisementForm(instance=ad)
    return render(request, 'ads-edit.html', {'form': form, 'object': ad})


@permission_required('ads.can_delete_advertisement')
def advertisement_delete(request, pk):
    ad = get_object_or_404(Advertisement, pk=pk)
    if request.method == 'POST':
        ad.delete()
        return redirect('ads:advertisement_list')
    return render(request, 'ads-delete.html', {'object': ad})


@permission_required('ads.can_view_advertisement')
def advertisement_statistic(request):
    ads = Advertisement.objects.all()
    return render(request, 'ads-statistic.html', {'ads': ads})
