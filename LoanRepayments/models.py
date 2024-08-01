from django.db import models

# Create your models here.
class LoanRepayment(models.Model):
    loan_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    repayment_date = models.DateField()

    def __str__(self):
        return f"Repayment of {self.amount} on {self.repayment_date} for {self.loan}"
