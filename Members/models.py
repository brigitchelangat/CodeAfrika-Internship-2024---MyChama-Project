from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    join_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
