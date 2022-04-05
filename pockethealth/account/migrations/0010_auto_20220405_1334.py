# Generated by Django 3.2.8 on 2022-04-05 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_patientregistermodel_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='practitioner',
        ),
        migrations.RemoveField(
            model_name='communication',
            name='practitioner',
        ),
        migrations.RemoveField(
            model_name='qualification',
            name='practitioner',
        ),
        migrations.RemoveField(
            model_name='telecom',
            name='practitioner',
        ),
        migrations.AddField(
            model_name='address',
            name='practitionerregistermodel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='account.practitionerregistermodel'),
        ),
        migrations.AddField(
            model_name='communication',
            name='practitionerregistermodel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communication', to='account.practitionerregistermodel'),
        ),
        migrations.AddField(
            model_name='humanname',
            name='practitionerregistermodel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='name', to='account.practitionerregistermodel'),
        ),
        migrations.AddField(
            model_name='practitionerregistermodel',
            name='active',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='practitionerregistermodel',
            name='birthDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='practitionerregistermodel',
            name='gender',
            field=models.CharField(blank=True, choices=[('1', 'male'), ('2', 'female'), ('3', 'other'), ('4', 'unknown')], max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='qualification',
            name='practitionerregistermodel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qualification', to='account.practitionerregistermodel'),
        ),
        migrations.AddField(
            model_name='telecom',
            name='practitionerregistermodel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telecom', to='account.practitionerregistermodel'),
        ),
    ]
