# Generated by Django 4.1.5 on 2023-02-01 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eApp', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phoneNumber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='totalPrice',
            field=models.IntegerField(),
        ),
    ]