from django.shortcuts import render, redirect, get_object_or_404
from .models import Fee
from .forms import AddFeeForm  


def fee_list(request):
    fees = Fee.objects.all()
    return render(request, 'fees/fee_list.html', {'fees': fees})

def add_fee(request):
    if request.method == 'POST':
        form = AddFeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fee_list')
    else:
        form = AddFeeForm()
    return render(request, 'fees/add_fee.html', {'form': form})

def edit_fee(request, fee_id):
    fee = get_object_or_404(Fee, id=fee_id)
    if request.method == 'POST':
        form = AddFeeForm(request.POST, instance=fee)
        if form.is_valid():
            form.save()
            return redirect('fee_list')
    else:
        form = AddFeeForm(instance=fee)
    return render(request, 'fees/edit_fee.html', {'form': form})

def delete_fee(request, fee_id):
    fee = get_object_or_404(Fee, id=fee_id)
    if request.method == 'POST':
        fee.delete()
        return redirect('fee_list')
    return render(request, 'fees/confirm_delete.html', {'fee': fee})
