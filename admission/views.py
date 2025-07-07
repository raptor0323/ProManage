from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Admission
from .forms import AddAdmissionForm

@login_required
def admission_list(request):
    admissions = Admission.objects.filter(created_by = request.user)
    return render(request, 'admission/admission_list.html', {
        'admissions' : admissions
    })

@login_required
def admission_detail(request, pk):
    admission = get_object_or_404(Admission, created_by = request.user, pk=pk)

    return render(request, 'admission/admission_detail.html', {
        'admission' : admission
    })

@login_required
def admission_add(request): 
    if request.method == 'POST':
        form = AddAdmissionForm(request.POST)

        if form.is_valid():
            lead = form.save(commit = False)
            lead.created_by = request.user
            lead.save()


            messages.success(request, "Admission was created successfully.")
            return redirect('admission_list')
    else:
        form = AddAdmissionForm()
    return render(request, 'admission/admission_add.html',{
        'form' : form
    })

@login_required
def admission_edit(request, pk):
    admission = get_object_or_404(Admission, pk=pk)

    if request.method == 'POST':
        form = AddAdmissionForm(request.POST, instance=admission)
        if form.is_valid():
            form.save()
            return redirect('admission_detail', pk=admission.pk)
    else:
        form = AddAdmissionForm(instance=admission)

    return render(request, 'admission/admission_edit.html', {  # <-- fix this line
        'form': form,
        'admission': admission,
    })

def admission_delete(request, pk):
    lead = get_object_or_404(Admission, created_by=request.user, pk=pk)
    lead.delete()

    messages.success(request, "Admission was deleted successfully.")
    return redirect('admission_list')  


