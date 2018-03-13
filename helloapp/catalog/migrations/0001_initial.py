# Generated by Django 2.0.3 on 2018-03-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=20)),
                ('manager', models.CharField(max_length=20)),
                ('contact_number', models.IntegerField()),
                ('contact_email', models.EmailField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField()),
                ('street_adress', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
                ('representative', models.CharField(max_length=20)),
                ('contact_number', models.IntegerField()),
                ('contact_email', models.EmailField(max_length=20)),
                ('donation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stage_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_in_crew', models.IntegerField()),
                ('sound_checked', models.BooleanField()),
                ('set_time', models.CharField(max_length=7)),
                ('number_of_band_members', models.IntegerField()),
                ('photo', models.CharField(max_length=1000)),
            ],
        ),
    ]