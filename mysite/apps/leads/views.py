from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Lead
from .forms import LeadForm


@permission_required('leads.can_view_lead')
def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'leads-list.html', {'leads': leads})


@permission_required('leads.can_add_lead')
def lead_create(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leads:lead_list')
    else:
        form = LeadForm()
    return render(request, 'leads-create.html', {'form': form})


@permission_required('leads.can_view_lead')
def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    return render(request, 'leads-detail.html', {'object': lead})


@permission_required('leads.can_change_lead')
def lead_update(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('leads:lead_detail', pk=lead.pk)
    else:
        form = LeadForm(instance=lead)
    return render(request, 'leads-edit.html', {'form': form, 'object': lead})


@permission_required('leads.can_delete_lead')
def lead_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        lead.delete()
        return redirect('leads:lead_list')
    return render(request, 'leads-delete.html', {'object': lead})
