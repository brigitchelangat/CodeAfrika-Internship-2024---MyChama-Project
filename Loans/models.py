from django.db import models

# Create your models here.

class Loan(models.Model):
    LOAN_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('repaid', 'Repaid'),
    ]

    member_id = models.IntegerField()
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=LOAN_STATUS_CHOICES)

    def __str__(self):
        return f"Loan of {self.loan_amount} to {self.member} on {self.loan_date}"