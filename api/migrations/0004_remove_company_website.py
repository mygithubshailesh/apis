# Generated by Django 4.1.5 on 2023-06-06 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='website',
        ),
    ]
