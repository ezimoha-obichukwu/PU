# Generated by Django 4.2.1 on 2023-05-10 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollingunit', '0005_party'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollingunit_result',
            name='party_score',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pollingunit_result',
            name='result_id',
            field=models.IntegerField(),
        ),
    ]
