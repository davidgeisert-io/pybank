# Generated by Django 4.1 on 2022-08-08 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_account_slug_alter_account_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
