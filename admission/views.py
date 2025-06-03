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

