# Generated by Django 4.2.1 on 2023-05-10 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pollinguint_Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.IntegerField(max_length=11)),
                ('polling_unit_uniqueid', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField(max_length=11)),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
    ]
