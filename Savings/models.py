from django.db import models

# Create your models here.
class Saving(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    ]

    member_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    transaction_date = models.DateField()

    def __str__(self):
        return f"{self.transaction_type.capitalize()} of {self.amount} on {self.transaction_date}"