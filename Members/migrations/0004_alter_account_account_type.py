# Generated by Django 5.0.7 on 2024-08-02 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0003_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No')], default=1, max_length=1),
        ),
    ]
