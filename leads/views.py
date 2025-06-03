from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddEnquiryForm
from .models import Lead
from admission.models import Admission

@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by = request.user, converted_to_admission = False)

    return render(request, 'leads/leads_list.html',{
        'leads' : leads
    })




@login_required
def leads_detail(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    #lead = Lead.objects.filter(created_by = request.user).get(pk=pk)
    return render(request, 'leads/leads_detail.html', {
        'lead': lead
    })

@login_required
def leads_delete(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()

    messages.success(request, "Enquiry was deleted successfully.")
    return redirect('leads_list')


@login_required
def leads_edit(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    if request.method == 'POST':
        form = AddEnquiryForm(request.POST, instance=lead)
         
        if form.is_valid():
            form.save()

            messages.success(request, "Enquiry was updated successfully.")
            return redirect('leads_list')
    else:
        form = AddEnquiryForm(instance=lead)
    
    return render(request, 'leads/leads_edit.html',{
    'form' : form
    })



@login_required
def add_lead(request): 
    if request.method == 'POST':
        form = AddEnquiryForm(request.POST)

        if form.is_valid():
            lead = form.save(commit = False)
            lead.created_by = request.user
            lead.save()


            messages.success(request, "Enquiry was created successfully.")
            return redirect('leads_list')
    else:
        form = AddEnquiryForm()
    return render(request, 'leads/add_lead.html',{
        'form' : form
    })



@login_required
def convert_to_admission(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    admission = Admission.objects.create(
        name = lead.name,
        email = lead.email,
        address = lead.address,
        created_by = request.user

    )

    lead.converted_to_admission = True
    lead.save()

    messages.success(request, "Enquiry was converted to admission!")
    return redirect('leads_list')