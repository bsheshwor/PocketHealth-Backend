# Generated by Django 3.2.8 on 2022-03-18 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20211022_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.CharField(choices=[('1', 'Home'), ('2', 'Work'), ('3', 'Temporary'), ('4', 'Billing')], max_length=225)),
                ('address_type', models.CharField(choices=[('1', 'Postal'), ('2', 'Physical'), ('3', 'Postal & Physical')], max_length=40)),
                ('text', models.CharField(max_length=500)),
                ('line', models.CharField(max_length=225)),
                ('city', models.CharField(max_length=225)),
                ('district', models.CharField(max_length=225)),
                ('state', models.CharField(max_length=225)),
                ('postalCode', models.CharField(max_length=225)),
                ('country', models.CharField(max_length=225)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('text', models.CharField(choices=[('A', 'Annulled'), ('D', 'Divorced'), ('I', 'Interlocutory'), ('L', 'Legally Separated'), ('M', 'Married'), ('P', 'Polygamous'), ('S', 'Never Married'), ('T', 'Domestic partner'), ('U', 'unmarried'), ('W', 'Widowed'), ('UNK', 'unknown')], max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_type', models.CharField(choices=[('1', 'replaced-by'), ('2', 'replaces'), ('3', 'refer'), ('4', 'seealso')], max_length=225)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
            ],
        ),
        migrations.CreateModel(
            name='HumanName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.CharField(choices=[('1', 'usual'), ('2', 'official'), ('3', 'temp'), ('4', 'nickname'), ('5', 'anonymous'), ('6', 'old'), ('7', 'maiden')], default='2', max_length=225)),
                ('text', models.CharField(max_length=225)),
                ('family', models.CharField(max_length=225)),
                ('given', models.CharField(max_length=225)),
                ('prefix', models.CharField(max_length=10)),
                ('suffix', models.CharField(max_length=225)),
                ('period', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.period')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Deceased',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deceasedBoolean', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ContactPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(choices=[('1', 'phone'), ('2', 'fax'), ('3', 'email'), ('4', 'pager'), ('5', 'url'), ('6', 'sms')], max_length=20)),
                ('value', models.CharField(max_length=255, null=True)),
                ('use', models.CharField(choices=[('1', 'Mobile'), ('2', 'Work'), ('3', 'Home'), ('4', 'Other')], max_length=255, null=True)),
                ('rank', models.IntegerField(null=True, verbose_name=50)),
                ('period', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.period')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.CharField(choices=[('C', 'Emergency Contact'), ('E', 'Employer'), ('F', 'Federal Agency'), ('I', 'Insurance Company'), ('N', 'Next-of-Kin'), ('S', 'State Agency'), ('U', 'Unknown')], max_length=225)),
                ('gender', models.CharField(choices=[('1', 'male'), ('2', 'female'), ('3', 'other'), ('4', 'unknown')], max_length=225)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.address')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.humanname')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.period')),
                ('telecom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.contactpoint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('ar', 'Arabic'), ('bn', 'Bengali'), ('cs', 'Czech'), ('da', 'Danish'), ('de', 'German'), ('de-AT', 'German (Austria)'), ('de-CH', 'German (Switzerland)'), ('de-DE', 'German (Germany)'), ('el', 'Greek'), ('en', 'English'), ('en-AU', 'English (Australia)'), ('en-CA', 'English (Canada)'), ('en-GB', 'English (Great Britain)'), ('en-IN', 'English (India)'), ('en-NZ', 'English (New Zeland)'), ('en-SG', 'English (Singapore)'), ('en-US', 'English (United States)'), ('es', 'Spanish'), ('es-AR', 'Spanish (Argentina)'), ('es-ES', 'Spanish (Spain)'), ('es-UY', 'Spanish (Uruguay)'), ('fi', 'Finnish'), ('fr', 'French'), ('fr-BE', 'French (Belgium)'), ('fr-CH', 'French (Switzerland)'), ('fr-FR', 'French (France)'), ('fy', 'Frysian'), ('fy-NL', 'Frysian (Netherlands)'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('it', 'Italian'), ('it-CH', 'Italian (Switzerland)'), ('it-IT', 'Italian (Italy)'), ('ja', 'Japanese'), ('ko', 'Korean'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nl-BE', 'Dutch (Belgium)'), ('nl-NL', 'Dutch (Netherlands)'), ('no', 'Norwegian'), ('no-NO', 'Norwegian (Norway)'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-BR', 'Portuguese (Brazil)'), ('ru', 'Russian'), ('ru-RU', 'Russian (Russia)'), ('sr', 'Serbian'), ('sr-RS', 'Serbian (Serbia)'), ('sv', 'Swedish'), ('sv-SE', 'Swedish (Sweden)'), ('te', 'Telegu'), ('zh', 'Chinese'), ('zh-CN', 'Chinese (China)'), ('zh-HK', 'Chinese (Hong Kong)'), ('zh-SG', 'Chinese (Singapore)'), ('zh-TW', 'Chinese (Taiwan)')], default='en-US', max_length=225)),
                ('preferred', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
            ],
        ),
    ]
