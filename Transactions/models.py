from django.db import models


TRANSACTION_TYPE_CHOICES = [
        (0, 'Deposit'),
        (1, 'Withdrawal'), 
        (2, 'Loan Repayment'), 
        (3, 'Interest'),  
        (4, 'Fines'),     
    ]

class Transaction(models.Model):
    account_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_reference = models.CharField(max_length=50)
    loan_id = models.IntegerField()
    transaction_type = models.IntegerField( choices=TRANSACTION_TYPE_CHOICES)
    transaction_date = models.DateField()

