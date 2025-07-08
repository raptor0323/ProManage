from django import forms
from .models import Fee

class AddFeeForm(forms.ModelForm):
    discount = forms.DecimalField(required=False, initial=0, min_value=0, max_value=100, label='Discount (%)', help_text='Enter discount percentage (0-100)')

    class Meta:
        model = Fee
        fields = ['student_name', 'course_name', 'total_fee', 'discount', 'paid_fee']

    def clean(self):
        cleaned_data = super().clean()
        total_fee = cleaned_data.get('total_fee')
        discount = cleaned_data.get('discount')
        if discount is None:
            discount = 0
        if discount > 100:
            self.add_error('discount', 'Discount percentage cannot be more than 100.')
        if total_fee is not None and discount < 0:
            self.add_error('discount', 'Discount cannot be negative.')
        return cleaned_data

    def clean_discount(self):
        discount = self.cleaned_data.get('discount')
        if discount is None:
            return 0
        return discount
