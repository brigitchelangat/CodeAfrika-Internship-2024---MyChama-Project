# Generated by Django 5.0.7 on 2024-08-02 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0004_alter_account_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.IntegerField(choices=[(0, 'Business'), (1, 'Member')], default=1),
        ),
    ]
