# Generated by Django 4.2.3 on 2023-09-29 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0003_remove_letter_updated_letter_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='sent',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
