from django.db import models


ACTIVE_STATUS_CHOICES = [
        (0, 'Yes'),
        (1, 'No'),    
    ]

IS_STAFF_CHOICES = [
        (0, 'Yes'),
        (1, 'No'),    
    ]

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_no = models.IntegerField(default=0)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    profession = models.CharField(max_length=50,default="Unspecified")
    joining_date = models.DateField()
    is_active = models.CharField(max_length=5, choices=ACTIVE_STATUS_CHOICES, default=0)
    is_staff = models.CharField(max_length=5, choices=IS_STAFF_CHOICES, default=1)

