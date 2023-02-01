# Generated by Django 4.1.5 on 2023-02-01 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.JSONField()),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('phoneNumber', models.IntegerField(max_length=20)),
                ('totalPrice', models.IntegerField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['items'],
            },
        ),
    ]
