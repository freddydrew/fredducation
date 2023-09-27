# Generated by Django 4.2.3 on 2023-09-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=75),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='firstName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='lastName',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]