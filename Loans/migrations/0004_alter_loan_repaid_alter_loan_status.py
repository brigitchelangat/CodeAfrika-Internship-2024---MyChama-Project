# Generated by Django 5.0.7 on 2024-08-02 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loans', '0003_loan_amount_due_loan_comments_loan_interest_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='repaid',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No')], default=1),
        ),
        migrations.AlterField(
            model_name='loan',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Rejected')]),
        ),
    ]
