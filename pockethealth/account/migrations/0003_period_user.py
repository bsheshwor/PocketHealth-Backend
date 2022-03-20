# Generated by Django 3.2.8 on 2022-03-20 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_period_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='period',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='period', to='account.customer'),
            preserve_default=False,
        ),
    ]