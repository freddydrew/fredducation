# Generated by Django 4.2.3 on 2023-09-18 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(editable=False, max_length=75),
        ),
    ]
