from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from admission.models import Admission


class AddAdmissionForm(forms.ModelForm):
    class Meta :
        model = Admission
        fields = ('name', 'father_name','mother_name','date_of_birth',
                  'gender','email', 'address', 'courses_interested','academic_qualification',
                  'mobile_no','known_languages','enquiry_via', )