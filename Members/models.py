from django.db import models


ACTIVE_STATUS_CHOICES = [
        (0, 'Yes'),
        (1, 'No'),    
    ]

IS_STAFF_CHOICES = [
        (0, 'Yes'),
        (1, 'No'),    
    ]

ACC_TYPE_CHOICES = [
        (0, 'Business'),
        (1, 'Member'),    
    ]

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_no = models.IntegerField(default=0)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    profession = models.CharField(max_length=50,default="Unspecified")
    joining_date = models.DateField()
    is_active = models.IntegerField(choices=ACTIVE_STATUS_CHOICES, default=0)
    is_staff = models.IntegerField(choices=IS_STAFF_CHOICES, default=1)


class Account(models.Model):
    member_id= models.IntegerField()
    account_number= models.IntegerField()
    actual_balance = models.DecimalField(max_digits=10, decimal_places=2)
    available_balance = models.DecimalField(max_digits=10, decimal_places=2)
    account_type = models.IntegerField( choices=ACC_TYPE_CHOICES, default=1)