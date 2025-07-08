from django.db import models

class Fee(models.Model):
    student_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # now percentage
    paid_fee = models.DecimalField(max_digits=10, decimal_places=2)
    due_fee = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    payment_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        discount_amount = (self.total_fee * self.discount) / 100
        self.due_fee = self.total_fee - discount_amount - self.paid_fee
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student_name} - {self.course_name}"
