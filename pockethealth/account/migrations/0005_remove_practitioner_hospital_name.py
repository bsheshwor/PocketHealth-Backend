# Generated by Django 3.2.8 on 2022-04-05 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20220405_0711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practitioner',
            name='hospital_name',
        ),
    ]