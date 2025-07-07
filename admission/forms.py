from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from admission.models import Admission


class AddAdmissionForm(forms.ModelForm):
    class Meta :
        model = Admission
        fields = ('name', 'father_name','mother_name','date_of_birth',
                  'gender','email', 'address', 'courses_interested','academic_qualification',
                  'mobile_no','known_languages','enquiry_via', )
        widgets = {
            'name': forms.TextInput(attrs={'id': 'id_name'}),
            'father_name': forms.TextInput(attrs={'id': 'id_father_name'}),
            'mother_name': forms.TextInput(attrs={'id': 'id_mother_name'}),
            'date_of_birth': forms.DateInput(attrs={'id': 'id_date_of_birth', 'type': 'date'}),
            'gender': forms.Select(attrs={'id': 'id_gender'}),
            'email': forms.EmailInput(attrs={'id': 'id_email'}),
            'address': forms.Textarea(attrs={'id': 'id_address'}),
            'courses_interested': forms.SelectMultiple(attrs={'id': 'id_courses_interested'}),
            'academic_qualification': forms.TextInput(attrs={'id': 'id_academic_qualification'}),
            'mobile_no': forms.TextInput(attrs={'id': 'id_mobile_no'}),
            'known_languages': forms.SelectMultiple(attrs={'id': 'id_known_languages'}),
            'enquiry_via': forms.Select(attrs={'id': 'id_enquiry_via'}),
        }