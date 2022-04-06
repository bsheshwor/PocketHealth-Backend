# Generated by Django 3.2.8 on 2022-03-21 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=225, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True, null=True)),
                ('end', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.user')),
                ('occupation', models.CharField(db_index=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('account.user', models.Model),
        ),
        migrations.CreateModel(
            name='Practitioner',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.user')),
                ('hospital_name', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('account.user', models.Model),
        ),
        migrations.CreateModel(
            name='HumanName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.CharField(blank=True, choices=[('1', 'usual'), ('2', 'official'), ('3', 'temp'), ('4', 'nickname'), ('5', 'anonymous'), ('6', 'old'), ('7', 'maiden')], default='2', max_length=225, null=True)),
                ('text', models.CharField(blank=True, max_length=225, null=True)),
                ('family', models.CharField(blank=True, max_length=225, null=True)),
                ('given', models.CharField(blank=True, max_length=225, null=True)),
                ('prefix', models.CharField(blank=True, max_length=10, null=True)),
                ('suffix', models.CharField(blank=True, max_length=225, null=True)),
                ('period', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.period')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='human_name', to='account.patient')),
            ],
        ),
        migrations.CreateModel(
            name='ContactPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(blank=True, choices=[('1', 'phone'), ('2', 'fax'), ('3', 'email'), ('4', 'pager'), ('5', 'url'), ('6', 'sms')], max_length=20, null=True)),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('use', models.CharField(blank=True, choices=[('1', 'Mobile'), ('2', 'Work'), ('3', 'Home'), ('4', 'Other')], max_length=255, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('period', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.period')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_point', to='account.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.CharField(blank=True, choices=[('1', 'Home'), ('2', 'Work'), ('3', 'Temporary'), ('4', 'Billing')], max_length=225, null=True)),
                ('address_type', models.CharField(blank=True, choices=[('1', 'Postal'), ('2', 'Physical'), ('3', 'Postal & Physical')], max_length=40, null=True)),
                ('text', models.CharField(blank=True, max_length=500, null=True)),
                ('line', models.CharField(blank=True, max_length=225, null=True)),
                ('city', models.CharField(blank=True, max_length=225, null=True)),
                ('district', models.CharField(blank=True, max_length=225, null=True)),
                ('state', models.CharField(blank=True, max_length=225, null=True)),
                ('postalCode', models.CharField(blank=True, max_length=225, null=True)),
                ('country', models.CharField(blank=True, max_length=225, null=True)),
                ('period', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.period')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='account.patient')),
            ],
        ),
        migrations.AddField(
            model_name='period',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='period', to='account.patient'),
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=15, null=True)),
                ('text', models.CharField(blank=True, choices=[('A', 'Annulled'), ('D', 'Divorced'), ('I', 'Interlocutory'), ('L', 'Legally Separated'), ('M', 'Married'), ('P', 'Polygamous'), ('S', 'Never Married'), ('T', 'Domestic partner'), ('U', 'unmarried'), ('W', 'Widowed'), ('UNK', 'unknown')], max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marital_status', to='account.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_type', models.CharField(blank=True, choices=[('1', 'replaced-by'), ('2', 'replaces'), ('3', 'refer'), ('4', 'seealso')], max_length=225, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='link', to='account.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Deceased',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deceasedBoolean', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deceased', to='account.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.CharField(blank=True, choices=[('C', 'Emergency Contact'), ('E', 'Employer'), ('F', 'Federal Agency'), ('I', 'Insurance Company'), ('N', 'Next-of-Kin'), ('S', 'State Agency'), ('U', 'Unknown')], max_length=225, null=True)),
                ('gender', models.CharField(blank=True, choices=[('1', 'male'), ('2', 'female'), ('3', 'other'), ('4', 'unknown')], max_length=225, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.address')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.humanname')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.period')),
                ('telecom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.contactpoint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='account.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, choices=[('ar', 'Arabic'), ('bn', 'Bengali'), ('cs', 'Czech'), ('da', 'Danish'), ('de', 'German'), ('de-AT', 'German (Austria)'), ('de-CH', 'German (Switzerland)'), ('de-DE', 'German (Germany)'), ('el', 'Greek'), ('en', 'English'), ('en-AU', 'English (Australia)'), ('en-CA', 'English (Canada)'), ('en-GB', 'English (Great Britain)'), ('en-IN', 'English (India)'), ('en-NZ', 'English (New Zeland)'), ('en-SG', 'English (Singapore)'), ('en-US', 'English (United States)'), ('es', 'Spanish'), ('es-AR', 'Spanish (Argentina)'), ('es-ES', 'Spanish (Spain)'), ('es-UY', 'Spanish (Uruguay)'), ('fi', 'Finnish'), ('fr', 'French'), ('fr-BE', 'French (Belgium)'), ('fr-CH', 'French (Switzerland)'), ('fr-FR', 'French (France)'), ('fy', 'Frysian'), ('fy-NL', 'Frysian (Netherlands)'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('it', 'Italian'), ('it-CH', 'Italian (Switzerland)'), ('it-IT', 'Italian (Italy)'), ('ja', 'Japanese'), ('ko', 'Korean'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nl-BE', 'Dutch (Belgium)'), ('nl-NL', 'Dutch (Netherlands)'), ('no', 'Norwegian'), ('no-NO', 'Norwegian (Norway)'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-BR', 'Portuguese (Brazil)'), ('ru', 'Russian'), ('ru-RU', 'Russian (Russia)'), ('sr', 'Serbian'), ('sr-RS', 'Serbian (Serbia)'), ('sv', 'Swedish'), ('sv-SE', 'Swedish (Sweden)'), ('te', 'Telegu'), ('zh', 'Chinese'), ('zh-CN', 'Chinese (China)'), ('zh-HK', 'Chinese (Hong Kong)'), ('zh-SG', 'Chinese (Singapore)'), ('zh-TW', 'Chinese (Taiwan)')], default='en-US', max_length=225, null=True)),
                ('preferred', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communication', to='account.patient')),
            ],
        ),
    ]
