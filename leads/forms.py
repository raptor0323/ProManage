from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .models import Lead


class AddEnquiryForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={'type': 'date'}
        )
    )
    class Meta :
        model = Lead
        fields = ('name', 'father_name','mother_name','date_of_birth',
                  'gender','email', 'address', 'courses_interested','academic_qualification',
                  'mobile_no','known_languages','enquiry_via','priority','facalty' )