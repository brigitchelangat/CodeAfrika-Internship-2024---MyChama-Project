from django.db import models


class Loan(models.Model):
    LOAN_STATUS_CHOICES = [
        (0, 'Pending'),
        (1, 'Approved'),
        (2, 'Rejected'),
    ]
    REPAID_CHOICES = [
        (0, 'Yes'),
        (1, 'No'),
    ]

    member_id = models.IntegerField()
    ref_no = models.CharField(max_length=20,default="Unspecified")
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00)
    interest = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00)
    repaid_amount = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00)
    loan_balance = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00)
    loan_date = models.DateField()
    due_date = models.DateField()
    status = models.IntegerField(choices=LOAN_STATUS_CHOICES)
    comments = models.CharField(max_length=255,default="Unspecified")
    repaid = models.IntegerField(choices=REPAID_CHOICES, default=1)
