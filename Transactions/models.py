from django.db import models

"""
- id : number //
- account_id : number FOREIGN KEY references Accounts.id//
- amount : number
- loan_id : number (0 or number>0) //
- transaction_reference : text//
- transaction_type : choice (0-deposit,1-withdrawal,2-loanrepayment,3-interest,4-fines)////
- transaction_date : date//
"""

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
    transaction_type = models.CharField(max_length=5, choices=TRANSACTION_TYPE_CHOICES)
    transaction_date = models.DateField()

