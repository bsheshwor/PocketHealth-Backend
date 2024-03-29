# Generated by Django 3.2.8 on 2022-04-05 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20220405_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='annotation', to='account.note'),
        ),
        migrations.AlterField(
            model_name='note',
            name='careteam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='note', to='account.careteam'),
        ),
    ]
