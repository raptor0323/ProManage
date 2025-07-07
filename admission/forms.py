from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from admission.models import Admission


class AddAdmissionForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Admission
        fields = (
            'name', 'father_name', 'mother_name', 'date_of_birth',
            'gender', 'email', 'address', 'courses_interested',
            'academic_qualification', 'mobile_no',
            'known_languages', 'enquiry_via', 'priority','facalty'
        )
        widgets = {
            'courses_interested': CheckboxSelectMultiple(),
            'known_languages': CheckboxSelectMultiple(),
            'mobile_no': forms.TextInput(attrs={'placeholder': 'Enter mobile number'}),
        }
    def clean_mobile_no(self):
        mobile = self.cleaned_data.get('mobile_no')
        if mobile and not mobile.isdigit():
            raise forms.ValidationError("Enter digits only.")
        return mobile
