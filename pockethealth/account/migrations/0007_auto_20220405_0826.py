# Generated by Django 3.2.8 on 2022-04-05 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_patient_occupation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='communication',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='deceased',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='humanname',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='humanname',
            name='practitioner',
        ),
        migrations.RemoveField(
            model_name='link',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='maritalstatus',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='telecom',
            name='patient',
        ),
        migrations.CreateModel(
            name='PractitionerRegisterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practitioner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='practitioner', to='account.practitioner')),
            ],
        ),
        migrations.CreateModel(
            name='PatientRegisterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('1', 'male'), ('2', 'female'), ('3', 'other'), ('4', 'unknown')], max_length=225, null=True)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('patient', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='account.patient')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='patientregistermodel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='account.patientregistermodel'),
        ),
        migrations.AddField(
            model_name='communication',
            name='patientregistermodel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communication', to='account.patientregistermodel'),
        ),
        migrations.AddField(
            model_name='contact',
            name='patientregistermodel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='account.patientregistermodel'),
        ),
        migrations.AddField(
            model_name='deceased',
            name='patientregistermodel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deceased', to='account.patientregistermodel'),
        ),
        migrations.AddField(
            model_name='humanname',
            name='patientregistermodel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='name', to='account.patientregistermodel'),
        ),
        migrations.AddField(
            model_name='link',
            name='patientregistermodel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='link', to='account.patientregistermodel'),
        ),
        migrations.AddField(
            model_name='maritalstatus',
            name='patientregistermodel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maritalStatus', to='account.patientregistermodel'),
        ),
        migrations.AddField(
            model_name='organization',
            name='patientregistermodel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='managingOrganization', to='account.patientregistermodel'),
        ),
        migrations.AddField(
            model_name='telecom',
            name='patientregistermodel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telecom', to='account.patientregistermodel'),
        ),
    ]
