# Generated by Django 4.1.7 on 2023-03-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whitecardapp', '0006_application_it_return_approval'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='pancard_no',
            field=models.IntegerField(null=True),
        ),
    ]
