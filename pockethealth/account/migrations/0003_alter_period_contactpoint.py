# Generated by Django 3.2.8 on 2022-04-03 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20220403_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='contactpoint',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='period', to='account.contactpoint'),
        ),
    ]
