# Generated by Django 4.1.7 on 2023-03-06 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whitecardapp', '0002_application_applicant'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='ration_approval',
            field=models.CharField(default=False, max_length=10),
        ),
        migrations.AddField(
            model_name='application',
            name='rto_approval',
            field=models.CharField(default=False, max_length=10),
        ),
        migrations.AddField(
            model_name='application',
            name='voter_approval',
            field=models.CharField(default=False, max_length=10),
        ),
    ]