# Generated by Django 4.2.3 on 2023-07-20 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_articleimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumnail',
            field=models.ImageField(blank=True, upload_to='static/'),
        ),
    ]